(function(factory){
    if (typeof define === 'function' && define.amd) {
        define(['jquery','select2/dist/js/select2.full.min'], factory);
    } else {
        factory(jQuery);
    }
})(function ($){
    $.prototype.langcodes = function (originalValue) {
        var $select = $(this);
        if (originalValue) {
            $select.append(new Option(originalValue));
            $select.val(originalValue);
        }
        return $select.select2({
            minimumInputLength: 0,
            tags: true,
            ajax: {
                url: "/langcodes/langs.json",
                data: function (params) {
                    return {
                        term: params.term,
                    };
                },
                delay: 100,
                dataType: 'json',
                processResults: function(data, params) {
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
