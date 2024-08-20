document.getElementById('nominationForm')
    .addEventListener('submit', (event) => {
        event.preventDefault();

        let emptyFields = false;
        let radioGroups = document.querySelectorAll('#nominationForm input[type="radio"]');
        let checkedGroups = {};
        let missingGroups = [];

         radioGroups.forEach(function(radio) {
            if (!checkedGroups[radio.name]) {
                checkedGroups[radio.name] = false;
            }
            if (radio.checked) {
                checkedGroups[radio.name] = true;
            }
        });

        for (let key in checkedGroups) {
            if (!checkedGroups[key]) {
                emptyFields = true;
                 missingGroups.push(key);
            }
        }

        if (emptyFields) {
            let missingFieldsText = missingGroups.map(group => `<li>${group}</li>`).join('');
            document.getElementById('missingFieldsList').innerHTML = missingFieldsText;

            let emptyFieldsModal = new bootstrap.Modal(document.getElementById('emptyFieldsModal'));
            emptyFieldsModal.show();

            document.getElementById('confirmSubmit')
                .addEventListener('click', () => {
                    document.getElementById('nominationForm').submit();
                });
        } else {
            event.target.submit();
        }

});