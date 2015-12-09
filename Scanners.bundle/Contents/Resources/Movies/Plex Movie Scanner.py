#
# Copyright (c) 2010 Plex Development Team. All rights reserved.
#
import re, os, os.path
import Media, VideoFiles, Stack, Utils
SeriesScanner = __import__('Plex Series Scanner')

nice_match = '(.+) [\(\[]([1-2][0-9]{3})[\)\]]'
standalone_tv_regexs = [ '(.*?)( \(([0-9]+)\))? - ([0-9])+x([0-9]+)(-[0-9]+[Xx]([0-9]+))? - (.*)' ]

# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):

  file = 'C:\Test\Pling1.mp4'
  movie = Media.Movie('Star Wars: Episod II', '2002')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test.mp4'
  # movie = Media.Movie(name, year)
  movie = Media.Movie('Star Wars: The Force Awakens', '2015')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test2.mp4'
  movie = Media.Movie('Star Wars: Episod I', '1999')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)
