document.addEventListener('DOMContentLoaded', function() {
    var addNewSeries = document.getElementById('add-series');
    var newSeriesForm = document.getElementById('add-series-form');

    var updateSeries = document.getElementsByClassName('update-series');
    var updateSeriesForms = document.getElementsByClassName('update-series-form');

    addNewSeries.addEventListener('click', function(event) {
        newSeriesForm.style.display = 'block';
    });

    for (var i = 0; i < updateSeries.length; i++) {
        if (updateSeries[i]) {
            (function(index) {
                updateSeries[index].addEventListener('click', function(event) {
                    if (updateSeriesForms[index]) {
                        updateSeriesForms[index].style.display = (updateSeriesForms[index].style.display === 'block') ? 'none' : 'block';
                    }
                });
            })(i);
        }
    }

    document.addEventListener('click', function(event) {
    if (!newSeriesForm.contains(event.target) && event.target !== addNewSeries) {
        newSeriesForm.style.display = 'none';
        }

    for (var i = 0; i < updateSeriesForms.length; i++) {
        if (updateSeriesForms[i] && !updateSeriesForms[i].contains(event.target) && event.target !== updateSeries[i]) {
            updateSeriesForms[i].style.display = 'none';
            }
        }
    });
});
