document.addEventListener('DOMContentLoaded', function() {
    var addNewSeries = document.getElementById('add-series');
    var newSeriesForm = document.getElementById('add-series-form');

    var updateSeries = document.getElementById('update-series');
    var updateSeriesForm = document.getElementById('update-series-form');

    addNewSeries.addEventListener('click', function(event) {
        newSeriesForm.style.display = 'block';
    });

    updateSeries.addEventListener('click', function(event) {
        updateSeriesForm.style.display = 'block';
    });

    document.addEventListener('click', function(event) {
    if (!newSeriesForm.contains(event.target) && event.target !== addNewSeries) {
        newSeriesForm.style.display = 'none';
        }

    if (!updateSeriesForm.contains(event.target) && event.target !== updateSeries) {
        updateSeriesForm.style.display = 'none';
        }
    });
});