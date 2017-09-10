var express = require('express');
var child_process = require('child_process');
var bodyParser = require('body-parser');

var app = express();

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/solve', function(req, res) {
    var data = req.body.data;
    try {
      JSON.parse(data);
      // TODO: Danger, client data goes into exec -> should have better way to check the incomming data
      const child = child_process.execFile('python', ['./solver.py', data], (err, stdout, stderr) => {
        if (err) throw err;
        res.type('json');
        res.send( stdout )
      });
    }
    catch (e) {
      const child = child_process.execFile('python', ['./solver.py'], (err, stdout, stderr) => {
        if (err) throw err;
        res.type('json');
        res.send(stdout)
      });
    }
});

app.listen(8080, function () {
  console.log('App running on port 8080')
});
