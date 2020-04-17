// get pea office name -> change name in table view
var select = document.querySelector('select[name="choices"]');
select.addEventListener('change', function() {
    pea_office_id = event.target.value;
    pea_office_name = $("#office_selector option:selected").text();
    console.log("PEA Office ID: "+ pea_office_name + "= " + pea_office_id);
    // update pea office name upper table only!
    if (pea_office_name == 'กดเพื่อเลือก') {
        document.getElementById("choosee_pea_office").innerHTML = 'ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า';
        destroy_table_data();
    } else {
        document.getElementById("choosee_pea_office").innerHTML = pea_office_name;
        create_table_data();
        }
  });

// object literal holding data for option elements
var Select_List_Data = {
    
    'choices': { // name of associated select box
        
        // names match option values in controlling select box
        None: {
            text: ['กรุณาเลือกสำนักงานการไฟฟ้า'],
            value: ['กรุณาเลือกสำนักงานการไฟฟ้า']
        },
        N1: {
            text: ['กดเพื่อเลือก', 'กฟฟ.เชียงใหม่', 'กฟจ.เชียงใหม่ 2', 'กฟจ.เชียงราย', 'กฟจ.ลำปาง', 'กฟจ.ลำพูน', 'กฟจ.พะเยา', 'กฟจ.แม่ฮ่องสอน',
                   'กฟอ.สันทราย', 'กฟอ.แม่ริม', 'กฟอ.ฝาง', 'กฟอ.จอมทอง', 'กฟอ.สันป่าตอง', 'กฟอ.แม่สาย', 'กฟอ.เทิง', 'กฟอ.เกาะคา'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'กฟฟ.เชียงใหม่', 'กฟจ.เชียงใหม่ 2', 'กฟจ.เชียงราย', 'กฟจ.ลำปาง', 'กฟจ.ลำพูน', 'กฟจ.พะเยา', 'กฟจ.แม่ฮ่องสอน',
                    'กฟอ.สันทราย', 'กฟอ.แม่ริม', 'กฟอ.ฝาง', 'กฟอ.จอมทอง', 'กฟอ.สันป่าตอง', 'กฟอ.แม่สาย', 'กฟอ.เทิง', 'กฟอ.เกาะคา']
        },
        N2: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        N3: {
            text: ['กดเพื่อเลือก', 'Iframes', 'PHP to JS', 'Object Literals', 'Initializing JS'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        NE1: {
            text: ['กดเพื่อเลือก', 'Scrolling Divs', 'Tooltips', 'Rotate Images', 'Scrollers', 'Banner Rotator'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'scroll', 'tooltips', 'rotate', 'scrollers', 'banner']
        },
        NE2: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        NE3: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        C1: {
            text: ['กดเพื่อเลือก', 'Scrolling Divs', 'Tooltips', 'Rotate Images', 'Scrollers', 'Banner Rotator'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'scroll', 'tooltips', 'rotate', 'scrollers', 'banner']
        },
        C2: {
            text: ['กดเพื่อเลือก','กฟฟ.พัทยา', 'กฟจ.ชลบุรี', 'กฟอ.บ้านบึง'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', '0806101', 'กฟจ.ชลบุรี', 'กฟอ.บ้านบึง']
        },
        C3: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        S1: {
            text: ['กดเพื่อเลือก', 'Scrolling Divs', 'Tooltips', 'Rotate Images', 'Scrollers', 'Banner Rotator'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'scroll', 'tooltips', 'rotate', 'scrollers', 'banner']
        },
        S2: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
        S3: {
            text: ['กดเพื่อเลือก', 'Random Image', 'Form Class', 'Table Class', 'Order Form'],
            value: ['ท่านยังไม่ได้เลือกพื้นที่การไฟฟ้า', 'random', 'form', 'table', 'order']
        },
    
    }    
};

// removes all option elements in select box 
// removeGrp (optional) boolean to remove optgroups
function removeAllOptions(sel, removeGrp) {
    var len, groups, par;
    if (removeGrp) {
        groups = sel.getElementsByTagName('optgroup');
        len = groups.length;
        for (var i=len; i; i--) {
            sel.removeChild( groups[i-1] );
        }
    }
    
    len = sel.options.length;
    for (var i=len; i; i--) {
        par = sel.options[i-1].parentNode;
        par.removeChild( sel.options[i-1] );
    }
}

function appendDataToSelect(sel, obj) {
    var f = document.createDocumentFragment();
    var labels = [], group, opts;
    
    function addOptions(obj) {
        var f = document.createDocumentFragment();
        var o;
        
        for (var i=0, len=obj.text.length; i<len; i++) {
            o = document.createElement('option');
            o.appendChild( document.createTextNode( obj.text[i] ) );
            
            if ( obj.value ) {
                o.value = obj.value[i];
            }
            
            f.appendChild(o);
        }
        return f;
    }
    
    if ( obj.text ) {
        opts = addOptions(obj);
        f.appendChild(opts);
    } else {
        for ( var prop in obj ) {
            if ( obj.hasOwnProperty(prop) ) {
                labels.push(prop);
            }
        }
        
        for (var i=0, len=labels.length; i<len; i++) {
            group = document.createElement('optgroup');
            group.label = labels[i];
            f.appendChild(group);
            opts = addOptions(obj[ labels[i] ] );
            group.appendChild(opts);
        }
    }
    sel.appendChild(f);
}

// anonymous function assigned to onchange event of controlling select box
document.forms['demoForm'].elements['category'].onchange = function(e) {
    // name of associated select box
    var relName = 'choices';
    
    // reference to associated select box 
    var relList = this.form.elements[ relName ];
    
    // get data from object literal based on selection in controlling select box (this.value)
    var obj = Select_List_Data[ relName ][ this.value ];
    
    // remove current option elements
    removeAllOptions(relList, true);
    
    // call function to add optgroup/option elements
    // pass reference to associated select box and data for new options
    // console.log(relList);
    // console.log(obj['value'][0]);

    if (obj['value'][0] == 'กรุณาเลือกสำนักงานการไฟฟ้า') {
        destroy_table_data();
    } else {
        // console.log(obj['value'][0])
        appendDataToSelect(relList, obj);
        document.getElementById("choosee_pea_office").innerHTML = obj['value'][0];
        destroy_table_data();
    }
};


// populate associated select box as page loads
(function() { // immediate function to avoid globals
    
    var form = document.forms['demoForm'];
    
    // reference to controlling select box
    var sel = form.elements['category'];
    sel.selectedIndex = 0;
    
    // name of associated select box
    var relName = 'choices';
    // reference to associated select box
    var rel = form.elements[ relName ];
    
    // get data for associated select box passing its name
    // and value of selected in controlling select box
    var data = Select_List_Data[ relName ][ sel.value ];    

    // add options to associated select box
    appendDataToSelect(rel, data);

    document.getElementById("choosee_pea_office").innerHTML = data['value'][0];
}());

// Create data table: get data from backend
function create_table_data() {
    let html_result = '';
    let table_body = '<tbody>';
    let table_body_end = '</tbody>';
    let table_row = '<tr>';
    let table_row_end = '</tr>';
    let num_row = '<th scope=\"row\">';
    let num_row_end = '</th>';
    let table_data = '<td>';
    let table_data_end = '</td>';
    html_result = 
                //    data index 0   //
                table_row +  
                (num_row + '1' + num_row_end) +
                (table_data + '123456' + table_data_end) +
                (table_data + '211-90787-1222' + table_data_end) +
                (table_data + '250' + table_data_end) +
                (table_data + 'ABC' + table_data_end) +
                (table_data + 'Feeder 1' + table_data_end) +
                (table_data + '82' + table_data_end) +
                (table_data + 'show' + table_data_end) +
                table_row_end +
                //    data index 0   //
                //    data index 1   //
                table_row +  
                (num_row + '2' + num_row_end) +
                (table_data + '234152' + table_data_end) +
                (table_data + '211-90787-1222' + table_data_end) +
                (table_data + '315' + table_data_end) +
                (table_data + 'ABC' + table_data_end) +
                (table_data + 'Feeder 1' + table_data_end) +
                (table_data + '102' + table_data_end) +
                (table_data + 'show' + table_data_end) +
                table_row_end +
                //    data index 1   //
                //    data index 2   //
                table_row +  
                (num_row + '1' + num_row_end) +
                (table_data + '123456' + table_data_end) +
                (table_data + '211-90787-1222' + table_data_end) +
                (table_data + '160' + table_data_end) +
                (table_data + 'ABC' + table_data_end) +
                (table_data + 'Feeder 1' + table_data_end) +
                (table_data + '72' + table_data_end) +
                (table_data + 'show' + table_data_end) +
                table_row_end +
                //    data index 2   //
                //    data index 3   //
                table_row +  
                (num_row + '2' + num_row_end) +
                (table_data + '234152' + table_data_end) +
                (table_data + '211-90787-1222' + table_data_end) +
                (table_data + '315' + table_data_end) +
                (table_data + 'ABC' + table_data_end) +
                (table_data + 'Feeder 1' + table_data_end) +
                (table_data + '132' + table_data_end) +
                (table_data + 'show' + table_data_end) +
                table_row_end
                //    data index 3   //
    document.getElementById('datatable').innerHTML = html_result;
    document.getElementById("datatable").style.visibility = "visible";
}

function destroy_table_data() {
    let html_result = '';
    document.getElementById('datatable').innerHTML = html_result;
    document.getElementById("datatable").style.visibility = "visible";   
}