jQuery.prototype.langcodes = function() {
    return this.select2({
        minimumInputLength: 0,
        delay: 100,
        initSelection: function(element, callback) {
            callback({
                id: element.val(),
                text: element.val(),
            });
        },
        ajax: {
            url: "/langcodes/langs.json",
            data: function(term) {
                return {
                    term: term,
                };
            },
            dataType: 'json',
            results: function(data) {
                return {
                    results: $.map(data, function(item) {
                        return {
                            text: item.code + " (" + item.name + ") ",
                            id: item.code,
                        };
                    }),
                };
            },
            cache: true,
        },
    });
}
