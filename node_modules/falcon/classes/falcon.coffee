###
Falcon framework
###
express = require 'express'
_       = require 'underscore'
_s      = require 'underscore.string'
fs      = require 'fs'
path    = require 'path'

falcon = () ->
  app = express()
  _.extend @, app

  # Inits the module arrays
  @modules = []
  @modulesTree = {}

  @

###
Add the module folder if theys exists.
###
falcon.prototype.addModule = (module) ->

  resolvedModulePath = path.resolve './', module

  if fs.existsSync(resolvedModulePath)
    @modules.push resolvedModulePath
  else
    throw "This module path(#{resolvedModulePath}) doesn't exists."

###
Init the modules
###
falcon.prototype.initModules = () ->

  for m, i in @modules
    
    moduleBaseName = path.basename(m)

    @modulesTree[moduleBaseName] = {}
    @modulesTree[moduleBaseName].initFiles = []

    files = fs.readdirSync m
    for f, i in files
      
      resolved = path.resolve m, f
      stats = fs.statSync resolved

      if not stats.isDirectory()
        if _s.startsWith f, 'init'
          @modulesTree[moduleBaseName].initFiles.push f
        else
          console.log f, " doesn't is a init file."
      else
        if f == 'classes'
          readClassesDir resolved
        else if f == 'config'
          console.log 'Read config dir'
        else if f == 'views'
          console.log 'Read views dir'
        else if f == 'media'
          console.log 'Read media dir'

  console.log @modulesTree


readClassesDir = (dir) ->
  files = fs.readdirSync dir



module.exports = falcon
