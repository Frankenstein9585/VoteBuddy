$(document).ready(function(){
        $("input[type='text']").each(function() {
            $(this).autocomplete({
                source: function(request, response) {
                    $.ajax({
                        url: "{{ url_for('autocomplete') }}",
                        dataType: "json",
                        data: {
                            q: request.term
                        },
                        success: function(data) {
                            response($.map(data, function(item) {
                                return {
                                    label: item.label,
                                    value: item.label
                                };
                            }));
                        }
                    });
                },
                minLength: 2
            });
        });
    });