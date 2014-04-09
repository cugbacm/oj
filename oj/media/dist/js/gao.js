$(document).ready(function() {
	var oTable = $('#listProblem').dataTable({
		"bProcessing": true,
		"bServerSide": true,
		"sAjaxSource": "/index/gettest/",
		"iDisplayLength": 25,
		"sDom": '<"H"pfr>t<"F"il>',
		"bAutoWidth": false,
		"bStateSave": true,
		"oLanguage": {
			"sInfo": "_START_ to _END_ of _TOTAL_ problems",
			"sInfoEmpty": "No problems",
			"sInfoFiltered": " (filtering from _MAX_ total problems)"
		},
		"aaSorting": [[ 1, "asc" ]],
		"aoColumns": [
					{
						"sClass": "center oj",
						"bSortable": false
					},
					{
				
						"sClass": "center prob_num"
					},
					{
						"sClass": ""
					},
					{
						"sClass": "date",
						"bSortable": false
					},
					{
						"sClass": "source"
					}
			],
		"fnServerData": function ( sSource, aoData, fnCallback ) {
			$.ajax( {
				"dataType": 'json', 
				"type": "POST", 
				"url": sSource, 
				"data": aoData, 
				"success": fnCallback
			});
		},
		"fnRowCallback": function( nRow, aData ) {
		 
			return nRow;
		},
		"bJQueryUI": true,
		"sPaginationType": "full_numbers"
	});
	
 
	
});
