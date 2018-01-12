$(function () {
  let list = $('UL.my_list');
  $('DIV#add_item').click(function () {
    list.append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    list.children().last().remove();
  });

  $('DIV#clear_list').click(function () {
    list.children().remove();
  });
});
