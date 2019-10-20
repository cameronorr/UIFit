###
Basic example
###

falcon = require '../../classes/falcon'

app = new falcon()

app.addModule './basic-module'

app.initModules()

#console.log app