<!--
url: https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py
title: basic-pitch/basic_pitch/data/datasets/guitarset.py at main · spotify ...
query: NMP Basic Pitch GuitarSet F-measure
fetched: 2026-10-08T02:24:08.775Z
-->

[Skip to content](https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py#start-of-content)
                

You signed in with another tab or window. [Reload](https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py)
 to refresh your session. You signed out in another tab or window. [Reload](https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py)
 to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py)
 to refresh your session. Dismiss alert

                 

[](https://github.com/spotify/basic-pitch)

FilesExpand file tree


-----------------------

main

/

guitarset.py
============

Copy path

Blame

More file actions

Blame

More file actions

Latest commit
-------------

History
-------

[History](https://github.com/spotify/basic-pitch/commits/main/basic_pitch/data/datasets/guitarset.py)

[](https://github.com/spotify/basic-pitch/commits/main/basic_pitch/data/datasets/guitarset.py)
History

188 lines (154 loc) · 6.59 KB

main

/

guitarset.py
============

Copy path

Top

File metadata and controls
--------------------------

*   Code
    
*   Blame
    

188 lines (154 loc) · 6.59 KB

[Raw](https://github.com/spotify/basic-pitch/raw/refs/heads/main/basic_pitch/data/datasets/guitarset.py)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

#!/usr/bin/env python

\# encoding: utf-8

#

\# Copyright 2024 Spotify AB

#

\# Licensed under the Apache License, Version 2.0 (the "License");

\# you may not use this file except in compliance with the License.

\# You may obtain a copy of the License at

#

\# http://www.apache.org/licenses/LICENSE-2.0

#

\# Unless required by applicable law or agreed to in writing, software

\# distributed under the License is distributed on an "AS IS" BASIS,

\# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

\# See the License for the specific language governing permissions and

\# limitations under the License.

import argparse

import logging

import os

import random

import time

from typing import Any, List, Dict, Tuple, Optional

import apache\_beam as beam

import mirdata

from basic\_pitch.data import commandline, pipeline

class GuitarSetInvalidTracks(beam.DoFn):

def process(self, element: Tuple\[str, str\], \*args: Tuple\[Any, Any\], \*\*kwargs: Dict\[str, Any\]) \-> Any:

track\_id, split \= element

yield beam.pvalue.TaggedOutput(split, track\_id)

class GuitarSetToTfExample(beam.DoFn):

DOWNLOAD\_ATTRIBUTES \= \["audio\_mic\_path", "jams\_path"\]

def \_\_init\_\_(self, source: str, download: bool) \-> None:

self.source \= source

self.download \= download

def setup(self) \-> None:

import apache\_beam as beam

import mirdata

self.guitarset\_remote \= mirdata.initialize("guitarset", data\_home\=self.source)

self.filesystem \= beam.io.filesystems.FileSystems() \# TODO: replace with fsspec

if self.download:

self.guitarset\_remote.download()

def process(self, element: List\[str\], \*args: Tuple\[Any, Any\], \*\*kwargs: Dict\[str, Any\]) \-> List\[Any\]:

import tempfile

import mirdata

import numpy as np

import sox

from basic\_pitch.constants import (

AUDIO\_N\_CHANNELS,

AUDIO\_SAMPLE\_RATE,

FREQ\_BINS\_CONTOURS,

FREQ\_BINS\_NOTES,

ANNOTATION\_HOP,

N\_FREQ\_BINS\_NOTES,

N\_FREQ\_BINS\_CONTOURS,

)

from basic\_pitch.data import tf\_example\_serialization

logging.info(f"Processing {element}")

batch \= \[\]

for track\_id in element:

track\_remote \= self.guitarset\_remote.track(track\_id)

with tempfile.TemporaryDirectory() as local\_tmp\_dir:

guitarset\_local \= mirdata.initialize("guitarset", local\_tmp\_dir)

track\_local \= guitarset\_local.track(track\_id)

for attribute in self.DOWNLOAD\_ATTRIBUTES:

source \= getattr(track\_remote, attribute)

destination \= getattr(track\_local, attribute)

os.makedirs(os.path.dirname(destination), exist\_ok\=True)

with self.filesystem.open(source) as s, open(destination, "wb") as d:

d.write(s.read())

local\_wav\_path \= f"{track\_local.audio\_mic\_path}\_tmp.wav"

tfm \= sox.Transformer()

tfm.rate(AUDIO\_SAMPLE\_RATE)

tfm.channels(AUDIO\_N\_CHANNELS)

tfm.build(track\_local.audio\_mic\_path, local\_wav\_path)

duration \= sox.file\_info.duration(local\_wav\_path)

time\_scale \= np.arange(0, duration + ANNOTATION\_HOP, ANNOTATION\_HOP)

n\_time\_frames \= len(time\_scale)

note\_indices, note\_values \= track\_local.notes\_all.to\_sparse\_index(

time\_scale, "s", FREQ\_BINS\_NOTES, "hz"

)

onset\_indices, onset\_values \= track\_local.notes\_all.to\_sparse\_index(

time\_scale, "s", FREQ\_BINS\_NOTES, "hz", onsets\_only\=True

)

contour\_indices, contour\_values \= track\_local.multif0.to\_sparse\_index(

time\_scale, "s", FREQ\_BINS\_CONTOURS, "hz"

)

batch.append(

tf\_example\_serialization.to\_transcription\_tfexample(

track\_local.track\_id,

"guitarset",

local\_wav\_path,

note\_indices,

note\_values,

onset\_indices,

onset\_values,

contour\_indices,

contour\_values,

(n\_time\_frames, N\_FREQ\_BINS\_NOTES),

(n\_time\_frames, N\_FREQ\_BINS\_CONTOURS),

)

)

return \[batch\]

def create\_input\_data(

train\_percent: float, validation\_percent: float, seed: Optional\[int\] \= None

) \-> List\[Tuple\[str, str\]\]:

assert train\_percent + validation\_percent < 1.0, "Don't over allocate the data!"

\# Test percent is 1 - train - validation

validation\_bound \= train\_percent

test\_bound \= validation\_bound + validation\_percent

if seed:

random.seed(seed)

def determine\_split(index: int) \-> str:

if index < len(track\_ids) \* validation\_bound:

return "train"

elif index < len(track\_ids) \* test\_bound:

return "validation"

else:

return "test"

guitarset \= mirdata.initialize("guitarset")

guitarset.download(\["index"\])

track\_ids \= guitarset.track\_ids

random.shuffle(track\_ids)

return \[(track\_id, determine\_split(i)) for i, track\_id in enumerate(track\_ids)\]

def main(known\_args: argparse.Namespace, pipeline\_args: List\[str\]) \-> None:

time\_created \= int(time.time())

destination \= commandline.resolve\_destination(known\_args, time\_created)

input\_data \= create\_input\_data(known\_args.train\_percent, known\_args.validation\_percent, known\_args.split\_seed)

pipeline\_options \= {

"runner": known\_args.runner,

"job\_name": f"guitarset-tfrecords-{time\_created}",

"machine\_type": "e2-standard-4",

"num\_workers": 25,

"disk\_size\_gb": 128,

"experiments": \["use\_runner\_v2"\],

"save\_main\_session": True,

"sdk\_container\_image": known\_args.sdk\_container\_image,

"job\_endpoint": known\_args.job\_endpoint,

"environment\_config": known\_args.sdk\_container\_image,

}

pipeline.run(

pipeline\_options,

pipeline\_args,

input\_data,

GuitarSetToTfExample(known\_args.source, download\=True),

GuitarSetInvalidTracks(),

destination,

known\_args.batch\_size,

)

if \_\_name\_\_ \== "\_\_main\_\_":

parser \= argparse.ArgumentParser()

commandline.add\_default(parser, os.path.basename(os.path.splitext(\_\_file\_\_)\[0\]))

commandline.add\_split(parser)

known\_args, pipeline\_args \= parser.parse\_known\_args()

main(known\_args, pipeline\_args)

You can’t perform that action at this time.