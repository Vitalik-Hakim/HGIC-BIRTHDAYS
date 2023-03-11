// assuming you have an array of objects called 'students'
const students = [
  { id: 1, name: "Mark Anthony", day: 11, month: "May", yearGroup: "DP1" },
  { id: 2, name: "Jane Smith", day: 5, month: "August", yearGroup: "DP2" },
  // add more objects as needed
];

// get a reference to the table body element
const tbody = $("#data-table tbody");
alert("I workkk");
// loop over the array and create a new row for each object
students.forEach((student) => {
  const row = $("<tr>");

  // create a cell for each property and append it to the row
  $("<td>").text(student.id).appendTo(row);
  $("<td>").text(student.name).appendTo(row);
  $("<td>").text(student.day).appendTo(row);
  $("<td>").text(student.month).appendTo(row);
  $("<td>").text(student.yearGroup).appendTo(row);

  // create the action cell and append it to the row
  const actionCell = $("<td>").addClass("btn-table").appendTo(row);
  $("<button>").addClass("btn btn-danger").text("Delete").appendTo(actionCell);
  $("<button>").addClass("btn btn-warning").text("Update").appendTo(actionCell);

  // append the row to the table body
  row.appendTo(tbody);
});
