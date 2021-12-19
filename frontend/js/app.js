//import { data } from '/js/sequences.js';
//const sequences = data.sequences;

// Use of maps to iterate array using one-liners
//const names = sequences.map(post => post.name);
//const groups = sequences.map(post => post.sequence);

// Console output
console.log('%c Welcome to Python Fast API console', 'font-size: 36px; font-weight: bold');
let log = console.log;
let info = console.info;
let warn = console.warn;
let error = console.error;

// GET method: Fetch JSON data using AJAX(jQuery)
function getJSONQuery(data, response) {
  const url = 'http://localhost:8000/quadruplex';
  $.ajax({
    type : 'GET',
    url : url,
    async: true,
    cache: true,
    dataType: 'json',
    contentType: 'application/json',
    success: function(data) {
      handleSuccessData(data);
    },
    error: function(response) {
      handleErrorData(response);
    }
  });
};

// POST method: POST JSON data using AJAX(jQuery)
function postJSONData() {
  const url = 'http://localhost:8000/quadruplex';
  var lenOfSeqs = 28;
  var num = 0;

  var sendJsonData = {
    "sequences": []
  }

  for (var x = 1; x < lenOfSeqs; x++) {
    var nameInput = $('#nameInput'+x).val();
    var sequenceInput = $('#sequenceInput'+x).val();

    var sequenceObj = {
      "name": nameInput,
      "sequence": sequenceInput
    }

    sendJsonData.sequences.push(sequenceObj);
    num += x;
  }

  $.ajax({
    type : 'POST',
    url : url,
    async: true,
    cache: false,
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify(sendJsonData),
    success: function(data) {
      handlePostSuccessData(data);
    },
    error: function(response) {
      handleErrorData(response);
    }
  });
  return sendJsonData;
};

// Success query handler - HTTP 200 response
function handleSuccessData(data) {
  const sequences = data.sequences;
  var num = 1;
  var countStr = num.toString();

  for (var i in sequences) {
    var name = sequences[i].name,
        seq = sequences[i].sequence;

    $('#nameInput'+countStr).val(name);
    $('#sequenceInput'+countStr).val(seq);
    countStr++;
  }
  toastr.success('GET - Success!');
}

// Error query handler - HTTP response status code/text
function handleErrorData(response) {
  var statusCode = response.status,
      statusText = response.statusText;

  if ((statusCode === 0) || (statusCode <= 300)) {
    warn('Error:', statusCode, statusText);
    toastr.warn(statusText, statusCode, {timeOut: 5000});
  }
  else if (statusCode >= 400) {
    error('Error:', statusCode, statusText);
    toastr.error(statusText, statusCode, {timeOut: 5000});
  }
  else if (statusCode <= 500) {
    warn('Error:', statusCode, statusText);
    toastr.warn(statusText, statusCode, {timeOut: 5000});
  }
}

// Handle POST Success data
function handlePostSuccessData(data) {
  var sequences = data.sequences;
  var counter = 0;
  var num = 1;
  var countStr = num.toString();
  var nameOfSequence = [];
  var countRate = [];

  // Show when POST is successful
  $('#tableHeader').show();
  $('#extractData').show();
  $('#displayMyChart').show();

  for (var i in sequences) {
    var quadruplexes = sequences[i].quadruplexes;
    var name = sequences[i].name;
    var count = sequences[i].count;
    var num = 1;

    // Empty before appending
    $('#startend'+countStr).empty();

    // Display sequence name & count
    $('#seqName'+countStr).html('<td id="seqName'+countStr+'">'+name+'</td>');
    $('#countQuad'+countStr).html('<td id="countQuad'+countStr+'">'+count+'</td>');

    for (var i in quadruplexes) {
      var start = quadruplexes[i].start,
          end = quadruplexes[i].end;
  
      // Check var for undefined or null
      if ((start == undefined) || (end == undefined) || (start == null) || (end == null)) {
        // Display N/A
        $('#startend'+countStr).html('<td id="startend'+countStr+'">N/A</td>');
      }
      else {
        // Display sequence name & count
        $('#startend'+countStr).append('<td id="startend'+countStr+'">['+start+', '+end+']</td>');
      }
    }
    countStr++;

    nameOfSequence.push(name);
    countRate.push(count);
    counter += i;
  }

  // Initiate chart function & send params
  renderMyChart(nameOfSequence, countRate);
  toastr.success('POST - Success!');
  //return renderChart;
}


// Dark/Light Theme - Stored & Retrieved using localStorage 
function toggleTheme() {
  const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
  const currentTheme = localStorage.getItem('theme');
  // Check current theme and set theme from current theme stored
  if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
      toggleSwitch.checked = true;
    }
    else {
      toggleSwitch.checked = false;
    }
  }
  // Change theme along with chart background
  // Set localStore + change logo + chart options
  function switchTheme(e) {
    if (e.target.checked) {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark'); // localStore - dark
    }
    else {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light'); // localStore - light
    }    
  }
  // By default set to light theme
  toggleSwitch.addEventListener('change', switchTheme, false);
}

// Events are fired when the page has loaded
window.onload = function() {
  // Hide when loaded
  $('#tableHeader').hide();
  $('#extractData').hide();
  $('#displayMyChart').hide();

  toggleTheme();
  getJSONQuery();
};

// Buttons function
$(function() {
  // Find Quad Button click event
  $('#findQuad').on('click', function() {
    // Native JS Scroll down to end of page
    var scrollingElement = (document.scrollingElement || document.body)
    function scrollSmoothToBottom() {
      $(scrollingElement).animate({
        scrollTop: document.body.scrollHeight
      }, 200);
    }
    postJSONData();
    scrollSmoothToBottom();
  });

  // Back to Top button
  var btn = $('#button');
  $(window).scroll(function() {
    if ($(window).scrollTop() > 200) {
      btn.addClass('show');
    } else {
      btn.removeClass('show');
    }
  });
  btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '200');
  });
});

// Render MyChart canvas from Chart.js
function renderMyChart(nameOfSequence, countRate) {
  // Destroy exiting Chart Instance to reuse <canvas> element
  let chartStatus = Chart.getChart('myChart');
  if (chartStatus != undefined) {
    chartStatus.destroy();
  }

  const ctx = $('#myChart');
  const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: nameOfSequence, // Names of Sequences - x axis
      datasets: [{
        label: ['# of Count'],
        data: countRate, // Count of quads - y axis
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}