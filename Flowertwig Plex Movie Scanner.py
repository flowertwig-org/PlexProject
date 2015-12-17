#
# Copyright (c) 2015 Mattias Blomqvist (plex.dev@email.flowertwig.org). All rights reserved.
#
import re, os, os.path
import Media, VideoFiles, Stack, Utils
import sys
import json,urllib,urllib2,base64

#SeriesScanner = __import__('Plex Series Scanner')
MoviesScanner = __import__('Plex Movie Scanner')

nice_match = '(.+) [\(\[]([1-2][0-9]{3})[\)\]]'
standalone_tv_regexs = [ '(.*?)( \(([0-9]+)\))? - ([0-9])+x([0-9]+)(-[0-9]+[Xx]([0-9]+))? - (.*)' ]

AMT_JSON_URL = 'http://movietrailers.apple.com/trailers/home/feeds/%s.json'
ALL_VIDEOS_INC = '%s/includes/automatic.html'


# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):

  # Scan for video files.
  #VideoFiles.Scan(path, files, mediaList, subdirs, root)
#  try:
#	  test = MoviesScanner()
#	  test.Scan(path, files, mediaList, subdirs, root)
#  except:
#	print 'ERROR 1'

  try:
	  MoviesScanner.Scan(path, files, mediaList, subdirs, root)
  except:
	print 'ERROR 2'

  # Adding external source movies
  file = 'C:\Test\Test1.mp4'
  movie = Media.Movie('Star Wars: Episod II', '2002')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test2.mp4'
  movie = Media.Movie('Star Wars: Episod I', '1999')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test3.mp4'
  movie = Media.Movie('Star Wars: Episod III', '2005')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test4.mp4'
  movie = Media.Movie('Star Wars', '1977')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  file = 'C:\Test\Test5.mp4'
  movie = Media.Movie('Star Wars: Episod V', '1980')
  movie.source = VideoFiles.RetrieveSource(file)
  movie.parts.append(file)
  mediaList.append(movie)

  #file = 'C:\Test\Test.mp4'
  # movie = Media.Movie(name, year)
  #movie = Media.Movie('Star Wars: The Force Awakens', '2015')
  #movie.source = VideoFiles.RetrieveSource(file)
  #movie.parts.append(file)
  #mediaList.append(movie)


  #MoviesScanner.Scan(path, files, mediaList, subdirs, language, root, kwargs)

  genres = []

  #JSON.ObjectFromURL(AMT_JSON_URL % ('genres'))

  #for trailer in JSON.ObjectFromURL(AMT_JSON_URL % ('genres')):
  #  for genre in trailer['genre']:
  #    if genre not in genres:
  #      genres.append(genre)

#	genres.sort()

#	for genre in genres:
#		file = 'C:\Test\' + genre
#		movie = Media.Movie(genre)
#		movie.source = VideoFiles.RetrieveSource(file)
#		movie.parts.append(file)
#		mediaList.append(movie)
