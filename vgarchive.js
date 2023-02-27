var vgTimeSpent = window.prompt("Please Enter Time Spent Playing:");
var vgRecommend = window.prompt("Would you Recommend this Title?");
var vgGivenUp = window.prompt("Have you Stopped Playing the Game?");  
  

  
  
  
      c1.innerText = vgName
      c2.innerText = vgConsole
      c3.innerText = vgStatus
      c4.innerText = vgTimeSpent
      c5.innerText = vgRecommend
      c6.innerText = vgGivenUp
  
  
  
      row.appendChild(c1);
      row.appendChild(c2);
      row.appendChild(c3);
      row.appendChild(c4);
      row.appendChild(c5);
      row.appendChild(c6);
      
      // Append row to table body
      table.appendChild(row)
}
