
$.fn.ajaxSubmit = function(options) {
    /* Change a form's submission type to ajax */
    var defaults = {
        'onerror':function(){},
        'onsuccess':function(){},
        'onstart':function(){},
        'onend':function(){}
    };
    options = jQuery.extend(defaults, options);
    url = this.action;
    this.action = null;
    this.onsubmit = function(){return false;};
    this.submit(function(e){
        e.preventDefault();
        var params = {};
        var theform = $(this);
        $(this)
        .find("input[checked], input[type='text'], input[type='hidden'], input[type='password'], input[type='submit'], option[selected], textarea")
        .filter(":enabled")
        .each(function() {
            params[ this.name || this.id || this.parentNode.name || this.parentNode.id ] = this.value;
        });
        console.log(params);
        
        options['onstart']();
        var theurl = this.action;

        $.ajax({
            async:true,
            cache:false,
            data:params,
            dataType:'text',
            error:options['onerror'],
            success:function(result) {
                options['onend']();
                if (!result) return options['onerror']('no response');
                try {
                    var False = false,True=true,None=null;
                    eval('var object = '+result);
                } catch(e) {
                    return options['onerror']('json');
                }
                theform.find('.error').html('');
                if (object.error){
                    return options['onerror']('server: '+ object.error);
                } else if (object.errors) {
                    for (var name in object.errors){
                        theform.find('.'+name+'.error').html(
                                object.errors[name].join('<br/>')
                            );
                    }
                } else
                    options['onsuccess'](object);
            },
            type:'POST',
            url:theurl,
        });
        return false;
    });
    return this;
}
