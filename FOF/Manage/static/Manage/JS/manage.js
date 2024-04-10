  


  function ClickSeason(event) {
    // Lấy ID nút
    const buttonId = event.target.dataset.seasonId;
    // Gửi yêu cầu đến server
    const url = `/api/get-season-info/${buttonId}`;
    

    fetch(url)
      .then((response) => response.json())
      .then((data) => {

        // Cập nhật nội dung HTML
        const seasonInfoElement = document.querySelector("#season-info");
        seasonInfoElement.querySelector(".season_name").textContent = data.season_name;
        // seasonInfoElement.querySelector(".season-start-time").textContent = data.time_start;
        // seasonInfoElement.querySelector(".season-end-time").textContent = data.time_end;
        seasonInfoElement.querySelector(".season-profit").textContent = data.profit;


      });
  }


  function showLandInfo(landId) {
    // Gọi API hoặc thực hiện các thao tác khác để lấy dữ liệu cho landId cụ thể
    fetch(`/api/get-land-info/${landId}`)
      .then((response) => response.json())
      .then((landInfo) => {
        // Lấy phần tử map từ lớp .land__row
        var map = document.querySelector(".land__row .map"); 
        var area = document.getElementById('dientich');
        var pH_num = document.getElementById('pH'); 
        var doAm = document.getElementById('doam'); 
        // Điền dữ liệu vào phần tử map        
        map.innerHTML = landInfo.position;
        area.innerHTML = landInfo.area; 
        ph_dec = landInfo.ph / 14 * 100; 
        pH_num.style.width = ph_dec + '%';
        doAm.style.width = landInfo.moisture + '%';
      });
  }

  function ClickLand(event) {
    // Lấy seasonId từ event.target hoặc các thuộc tính khác của sự kiện
    const seasonId = event.target.dataset.seasonId;

    // Kiểm tra seasonId có tồn tại và hợp lệ
    if (seasonId) {
      // Construct the URL to fetch land data for the provided season ID
      const landUrl = `/api/get-land-by-season/${seasonId}`;

   
    // Fetch land data
    fetch(landUrl)
      .then((response) => response.json())
      .then((landData) => {
        // Update land information in the UI
        const landContainer = document.getElementById("land-container");
  
        // Clear previous land data (optional)
        landContainer.innerHTML = ""; // Uncomment if you want to clear previous content
  
        // Process and display land data
        for (const landItem of landData) {
          // Create a new land element (div)
          const landElement = document.createElement("div");
          landElement.classList.add("land__item", "col-2");

          // Add land ID as a data attribute to the land element
          landElement.setAttribute("data-land-id", landItem.id);
  
          // Add land name
          const landName = document.createElement("p");
          landName.innerHTML = landItem.name;
          landName.style.fontWeight = "bold";
          landName.style.marginBottom = "10px";
          landElement.appendChild(landName);
  
          // Add land status (assuming a "status" property is returned from the API)
          const landStatus = document.createElement("div");
          landStatus.classList.add("land__status");
          landStatus.classList.add("green");
          landStatus.textContent = "Normal";
          
          landElement.appendChild(landStatus);
          landElement.addEventListener("click", function(event) {
            const landId = this.dataset.landId;
            Earse(event);
            showLandInfo(landId); 
            ClickLandShowPlant(event);
            
            
          });
  
          // Append the land element to the container
          landContainer.appendChild(landElement);
        }
      });
    }
}

function Earse(event){
  var p = document.getElementById('plant');
  p.innerHTML = ' ';
}

function ClickLandShowPlant(event){
  // Lấy seasonId từ event.target hoặc các thuộc tính khác của sự kiện
  const landId = event.target.dataset.landId;

  // Kiểm tra seasonId có tồn tại và hợp lệ
  if (landId) {
    // Construct the URL to fetch land data for the provided season ID
    const plantURL = `/api/get-plant-by-land/${landId}`;
    fetch(plantURL)
    .then((response) => response.json())
    .then((plantData) => {
      
        var plantdiv = document.getElementById('plant');
        // Tạo phần tử h4 và gán nội dung
        var h4 = document.createElement('h4');
        h4.textContent = 'THÔNG TIN CÂY TRỒNG';

        // Tạo phần tử div có lớp "row p__row"
        var rowDiv = document.createElement('div');
        rowDiv.className = 'row p__row';

        // Tạo các phần tử div có lớp tương ứng và gán nội dung
        var col1 = document.createElement('div');
        col1.className = 'col-2 plant__id';
        col1.textContent = 'STT';

        var col2 = document.createElement('div');
        col2.className = 'col-3 plant__name';
        col2.textContent = 'Tên loại cây';

        var col3 = document.createElement('div');
        col3.className = 'col-3 plant__detail';
        col3.textContent = 'Thông tin chi tiết';

        var col4 = document.createElement('div');
        col4.className = 'col-2 plant__status';
        col4.textContent = 'Tình trạng';

        var col5 = document.createElement('div');
        col5.className = 'col-2 plant__time';
        col5.textContent = 'Thời gian thu hoạch';

        // Gắn các phần tử con vào phần tử cha
        rowDiv.appendChild(col1);
        rowDiv.appendChild(col2);
        rowDiv.appendChild(col3);
        rowDiv.appendChild(col4);
        rowDiv.appendChild(col5);

        plantdiv.appendChild(h4);
        plantdiv.appendChild(rowDiv); 
        
        var cnt = 0;
        for (item of plantData){
          cnt++;
         // Tạo phần tử div có lớp "row p__row"
        var rowDiv = document.createElement('div');
        rowDiv.className = 'row p__row';

        // Tạo các phần tử div có lớp tương ứng và gán nội dung
        var col1 = document.createElement('div');
        col1.className = 'col-2 plant__id';
        col1.textContent = cnt;

        var col2 = document.createElement('div');
        col2.className = 'col-3 plant__name';
        col2.textContent = item.name;

        var col3 = document.createElement('div');
        col3.className = 'col-3 plant__detail';
        


        // Tạo phần tử ul
        var ul = document.createElement('ul');

        // Tạo các phần tử li và gán nội dung
        var loaiCayTrong = document.createElement('li');
        loaiCayTrong.textContent = 'Loại cây trồng: ' + typePlant(item.type);

        var thoiGianPhatTrien = document.createElement('li');
        thoiGianPhatTrien.textContent = 'Thời gian phát triển: ' + item.timeDev + ' tháng';

        var chuKyBonPhan = document.createElement('li');
        chuKyBonPhan.textContent = 'Chu kỳ bón phân: ' + item.bp + ' tháng';

        var nongDoKhoang = document.createElement('li');
        nongDoKhoang.textContent = 'Nồng độ khoáng cần thiết: ' + item.nd;

        // Gắn các phần tử li vào phần tử ul
        ul.appendChild(loaiCayTrong);
        ul.appendChild(thoiGianPhatTrien);
        ul.appendChild(chuKyBonPhan);
        ul.appendChild(nongDoKhoang);

        // Gắn phần tử ul vào phần tử col3
        col3.appendChild(ul);





        
        var col4 = document.createElement('div');
        col4.className = 'col-2 plant__status';
        col4.textContent = 'Tốt';

        var col5 = document.createElement('div');
        col5.className = 'col-2 plant__time';
        col5.textContent = '25 ngày';

        // Gắn các phần tử con vào phần tử cha
        rowDiv.appendChild(col1);
        rowDiv.appendChild(col2);
        rowDiv.appendChild(col3);
        rowDiv.appendChild(col4);
        rowDiv.appendChild(col5);

        plantdiv.appendChild(rowDiv); 
 
          
            
        }
       
      
    });
  }
}

function  typePlant(t){
  if (t == 0)
    return "Cây lương thực"; 
  else if (t == 1)
    return "Cây ăn quả"; 
  else 
    return "Cây rau củ";
}
  