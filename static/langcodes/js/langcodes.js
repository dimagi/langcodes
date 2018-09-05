(function(factory){

    if (typeof define === 'function' && define.amd) {
        define(['jquery','select2-3.4.5-legacy/select2.min'], factory);
    } else {
        factory(jQuery);
    }

})(function($){
    $.prototype.langcodes = function() {
        return this.select2({
            minimumInputLength: 0,
            delay: 100,
            initSelection: function(element, callback) {
                callback({
                    id: element.val(),
                    text: element.val(),
                });
            },
            // Allow manually entered text in drop down, which is not supported by legacy select2.
            createSearchChoice: function(term, data) {
                if (!_.find(data, function(d) { return d.text === term; })) {
                    return {
                        id: term,
                        text: term,
                    };
                }
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
    };

});
