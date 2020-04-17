var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: ['2563', '2564', '2565', '2566', '2567'],
        datasets: [{
            label: 'Full Capacity Overload',
            backgroundColor: 'rgb(176, 229, 124, 0.5)',
            borderColor: 'rgb(176, 229, 124)',
            data: [500, 600, 750, 850, 1000,]
        },
        {
            label: 'Phase Capacity Overload',
            backgroundColor: 'rgb(180, 216, 231, 0.5)',
            borderColor: 'rgb(180, 216, 231)',
            data: [400, 380, 520, 700, 800,]
        },
        {
            label: 'Under-Voltage',
            backgroundColor: 'rgb(255, 99, 132, 0.5)',
            borderColor: 'rgb(255, 99, 132)',
            data: [400, 420, 520, 610, 720,]
        },
    ]
    },
    // Configuration options go here
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    min: 200,
                    suggestedMin: 200,
                    max: 240,
                    suggestedMax: 240
                }
            }]
        }
    }

});