document.getElementById('nominationForm')
    .addEventListener('submit', (event) => {
        event.preventDefault();

        let emptyFields = false;
        let inputs = document.querySelectorAll('#nominationForm input[type="text"]');

        inputs.forEach((input) => {
            if (input.value.trim() === '')
                emptyFields = true;
        });

        if (emptyFields) {
            let emptyFieldsModal = new bootstrap.Modal(document.getElementById('emptyFieldsModal'));
            emptyFieldsModal.show();

            document.getElementById('confirmSubmit')
                .addEventListener('click', () => {
                    document.getElementById('nominationForm').submit();
                });
        } else {
            this.submit();
        }

});