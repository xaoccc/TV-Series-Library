document.addEventListener('DOMContentLoaded', function() {
    var addNewSeries = document.getElementById('add-series');
    var newSeriesForm = document.getElementById('add-series-form');

    if (newSeriesForm) {
        addNewSeries.addEventListener('click', function(event) {
            newSeriesForm.style.display = 'block';
        });
    }

    var updateSeries = document.getElementById('update-series');
    var updateSeriesForm = document.getElementById('update-series-form');
    var deleteSeries = document.getElementById('delete-series');

    if (updateSeriesForm) {
        updateSeries.addEventListener('click', function(event) {
            updateSeriesForm.style.display = 'block';
            updateSeries.style.display = 'none';
            deleteSeries.style.display = 'none';
        });
    }


    document.addEventListener('click', function(event) {
        if (newSeriesForm) {
            if (!newSeriesForm.contains(event.target) && event.target !== addNewSeries) {
                newSeriesForm.style.display = 'none';
            }
        }

        if (updateSeriesForm) {
            if (!updateSeriesForm.contains(event.target) && event.target !== updateSeries) {
                updateSeriesForm.style.display = 'none';
                updateSeries.style.display = 'block';
                deleteSeries.style.display = 'block';
            }
        }
    });
});
