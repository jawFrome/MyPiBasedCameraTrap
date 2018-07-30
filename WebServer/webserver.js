var http = require('http').createServer(LoadPage);
var fs = require('fs');

var imageDir = '/home/pi/CameraCaptures/';
console.log('Looking in ' + imageDir);
http.listen(8080);
console.log('Ready to load images');

function LoadPage(req, res)
{		
	res.writeHead(200, {'Content-Type' : 'text/html'}); 
	var html = '<!DOCTYPE html><html><body><h1>Camera Trap</h1><table style="width:100%">';
	html += '<tr><th>Image</th><th>Location</th></tr>';
	
	fs.readdir(imageDir, function(err, fileNames)
	{
		console.log('Found '+ fileNames.length + ' images');
		for(i=0;i<fileNames.length;i++)
		{
			html += '<tr><td>TODO Thumb Image</td><td>' + fileNames[i] + '</td></tr>';
		}

	html += '</table></body></html>'

	console.log('Returning ' + html);
	return res.end(html, 'utf-8');

	});

		
}



