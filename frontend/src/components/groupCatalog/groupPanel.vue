<template>
    <div class="container">
        <h1 class="title" id="title">Koło naukowe X</h1>
        <p class="p-category">Informatyka</p>
        <br>
        <div class="columns">
          <div class="column is-3">
            <b-button id="btn" tag="router-link" to="/forum">Forum</b-button>
            <br>
            <button type="button" class="button" id="btn" v-on:click="showAboutUs">O nas</button>
            <button type="button" class="button" id="btn" v-on:click="showWhatWeDo">Czym się zajmujemy</button>
            <button type="button" class="button" id="btn" v-on:click="showMembers">Członkowie</button>
            <button type="button" class="button" id="btn" v-on:click="showContact">Kontakt</button>
            <b-button id="btn" tag="router-link" to="/group-tutorials">Materiały dydaktyczne</b-button>
          </div>
          <div class="column is-7" id="centerDiv">
            <h2 class="centerDivHeader">O nas</h2>
            {{ this.aboutUs }}
          </div>
          <div class="column" id="divLinks">
            <b-menu :activable="false" :accordion="false" id="menu">
              <b-menu-list>
                <b-menu-item label="Linki">
                  <b-menu-item label="Github" target="_blank" href="https://github.com"></b-menu-item>
                  <b-menu-item label="Facebook" target="_blank" href="https://facebook.com"></b-menu-item>
                  <b-menu-item label="Discord" target="_blank" href="https://discord.com"></b-menu-item>
                </b-menu-item>
                <b-menu-item label="Dyski">
                  <b-menu-item label="Dysk 1" target="_blank" href="https://drive.google.com/drive/folders/1QMHnaSuOPcfOX16190I9D8q_Fa5pzeOF?usp=sharing"></b-menu-item>
                  <b-menu-item label="Dysk 2" target="_blank" href="https://drive.google.com/drive/folders/1vGf8f0nVkJcAZQ6S7mZ74vFhpJK0Gbeo?usp=sharing"></b-menu-item>
                </b-menu-item>
              </b-menu-list>
            </b-menu>
          </div>
          <!-- <Popup/> -->
        </div>
    </div>
</template>

<script>
// import Popup from "./components/popup/Popup.vue";

export default {
  name: "groupPanel",
  // components: {
  //   Popup,
  // },
  data() {
    return {
      aboutUs: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore. Ut placeat, exercitationem quas officia laudantium esse nobis blanditiis doloremque est eius quia fugit architecto ea deleniti animi consequuntur quis molestiae nulla commodi non facere quae distinctio aperiam? Esse dolorum ex illum tempora, neque labore explicabo pariatur odio accusamus impedit nesciunt eius similique quaerat consequuntur laudantium. Eveniet nulla omnis eligendi velit ut. Officia cupiditate fugit assumenda aliquam minima cumque perspiciatis dignissimos sapiente non. Ea repellendus sequi beatae esse illum, nulla voluptatem, ratione dolorum ducimus maxime ab minus veritatis optio illo quis amet voluptate obcaecati modi voluptatibus accusantium. Repudiandae laudantium nesciunt non omnis obcaecati quis iusto, dolorem laboriosam animi labore unde, quasi cumque libero? Sunt excepturi iste ipsum suscipit ex eveniet rerum! Magnam numquam impedit voluptatum culpa esse recusandae non optio laboriosam ipsum odit dicta pariatur rerum nobis, iure nostrum adipisci. At tempore quisquam non! Vero reprehenderit nostrum officiis quasi. Eaque quibusdam quaerat adipisci veritatis commodi pariatur beatae tenetur quae. Accusamus quo excepturi nam repellendus quis laborum quas suscipit? Aperiam incidunt dolore voluptas saepe praesentium quibusdam! Corrupti quas quaerat repellat, quia similique velit molestias. Recusandae sapiente sit quisquam laborum deleniti veritatis repellendus, magnam praesentium delectus inventore eum. Natus adipisci iusto ducimus error ipsum, ea neque, aliquid inventore odio cupiditate libero, dolor nulla? Cum ipsa totam officia obcaecati fugit, vel quae reprehenderit qui ducimus explicabo. Omnis ipsam doloremque cumque rem. Placeat voluptates vero eum sapiente quo, minus provident laborum saepe maiores quae necessitatibus alias ratione sint? Sed facere aspernatur ratione blanditiis! Porro commodi tempore voluptates eaque. Sunt est aspernatur sint error veritatis iusto aliquam voluptate quaerat rerum unde accusantium iste natus incidunt illo velit tempora dolorum ipsa et nostrum optio ratione nobis, temporibus qui! Ipsa, omnis officiis eveniet a cupiditate voluptas eos ducimus eius nostrum ab quos recusandae autem dicta possimus maxime aut quas dolor doloribus quia. Pariatur numquam doloribus officia voluptates ut quasi provident illum itaque ab quod! Obcaecati magnam molestiae nisi similique, amet praesentium reprehenderit itaque velit, consequuntur quos nam qui, architecto excepturi repudiandae ratione! Esse consequuntur, dolor laboriosam eaque, neque fugit a quam incidunt eos placeat quae nesciunt provident. Itaque veritatis non labore repellendus recusandae excepturi placeat. Itaque dolorem eveniet, assumenda explicabo ex delectus voluptatum beatae?',
      whatWeDo: '',
      members: '',
      contact: '',
      errors: []
    }
  },
  mounted() {
      document.title = 'Panel koła'
  },
  methods: {
    showAboutUs() {
      //this.aboutUs = 'O nas Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore. Ut placeat, exercitationem quas officia laudantium esse nobis blanditiis doloremque est eius quia fugit architecto ea deleniti animi consequuntur quis molestiae nulla commodi non facere quae distinctio aperiam? Esse dolorum ex illum tempora, neque labore explicabo pariatur odio accusamus impedit nesciunt eius similique quaerat consequuntur laudantium. Eveniet nulla omnis eligendi velit ut. Officia cupiditate fugit assumenda aliquam minima cumque perspiciatis dignissimos sapiente non. Ea repellendus sequi beatae esse illum, nulla voluptatem, ratione dolorum ducimus maxime ab minus veritatis optio illo quis amet voluptate obcaecati modi voluptatibus accusantium. Repudiandae laudantium nesciunt non omnis obcaecati quis iusto, dolorem laboriosam animi labore unde, quasi cumque libero? Sunt excepturi iste ipsum suscipit ex eveniet rerum! Magnam numquam impedit voluptatum culpa esse recusandae non optio laboriosam ipsum odit dicta pariatur rerum nobis, iure nostrum adipisci. At tempore quisquam non! Vero reprehenderit nostrum officiis quasi. Eaque quibusdam quaerat adipisci veritatis commodi pariatur beatae tenetur quae. Accusamus quo excepturi nam repellendus quis laborum quas suscipit? Aperiam incidunt dolore voluptas saepe praesentium quibusdam! Corrupti quas quaerat repellat, quia similique velit molestias. Recusandae sapiente sit quisquam laborum deleniti veritatis repellendus, magnam praesentium delectus inventore eum. Natus adipisci iusto ducimus error ipsum, ea neque, aliquid inventore odio cupiditate libero, dolor nulla? Cum ipsa totam officia obcaecati fugit, vel quae reprehenderit qui ducimus explicabo. Omnis ipsam doloremque cumque rem. Placeat voluptates vero eum sapiente quo, minus provident laborum saepe maiores quae necessitatibus alias ratione sint? Sed facere aspernatur ratione blanditiis! Porro commodi tempore voluptates eaque. Sunt est aspernatur sint error veritatis iusto aliquam voluptate quaerat rerum unde accusantium iste natus incidunt illo velit tempora dolorum ipsa et nostrum optio ratione nobis, temporibus qui! Ipsa, omnis officiis eveniet a cupiditate voluptas eos ducimus eius nostrum ab quos recusandae autem dicta possimus maxime aut quas dolor doloribus quia. Pariatur numquam doloribus officia voluptates ut quasi provident illum itaque ab quod! Obcaecati magnam molestiae nisi similique, amet praesentium reprehenderit itaque velit, consequuntur quos nam qui, architecto excepturi repudiandae ratione! Esse consequuntur, dolor laboriosam eaque, neque fugit a quam incidunt eos placeat quae nesciunt provident. Itaque veritatis non labore repellendus recusandae excepturi placeat. Itaque dolorem eveniet, assumenda explicabo ex delectus voluptatum beatae?'
      const container = document.getElementById('centerDiv');
      container.replaceChildren();

      const p = document.createElement('p');
      p.textContent = this.aboutUs;
      const h2 = document.createElement('h2');
      h2.textContent = 'O nas';
      h2.classList.add('centerDivHeader');
      container.append(h2, p);
    },
    showWhatWeDo() {
      this.whatWeDo = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae tenetur distinctio voluptatem molestias sapiente eum voluptatum perspiciatis adipisci? Adipisci voluptates ducimus in nulla quibusdam animi aspernatur dignissimos laboriosam ipsam nihil eveniet impedit dolorem ipsum ea nam, laborum incidunt assumenda voluptatum perferendis illo natus saepe obcaecati. Consequuntur ipsum nesciunt unde recusandae, dolor reiciendis veritatis sint excepturi repudiandae enim sequi, molestiae nobis neque perferendis. Illum molestias perspiciatis placeat totam, animi nostrum est exercitationem ad maxime! Amet modi possimus culpa neque consequatur quasi corporis optio veniam exercitationem voluptatibus fugit iure dicta ex quo facilis molestiae inventore atque, officiis maiores dolore a sapiente! Voluptates corporis voluptatum impedit. Praesentium, animi consequatur? Tenetur, expedita culpa accusantium non corporis autem rem unde eos tempore deleniti suscipit repellat repellendus quasi porro ullam veniam nulla quos eligendi, praesentium quaerat! Esse dolores totam, eaque temporibus quis itaque delectus dolor odio minima, natus adipisci laborum animi nesciunt architecto assumenda quae. Itaque cupiditate alias vitae molestiae harum enim ipsam possimus sapiente, qui hic vero odit velit amet autem, est doloribus ea soluta quasi voluptas! Suscipit officia vel doloremque, accusantium, soluta dolorem delectus at culpa aperiam laudantium non similique corrupti expedita earum hic quibusdam cum, sunt repudiandae! Ipsa nam quasi possimus aliquid, dignissimos eveniet, sed blanditiis nulla enim obcaecati labore mollitia dolor ullam magni praesentium reiciendis quibusdam molestias adipisci neque, ducimus maxime a corrupti. Reiciendis, non magnam! Quibusdam nulla veniam a quae, nemo, velit dicta reprehenderit animi maxime, sequi nihil sapiente obcaecati reiciendis quas doloribus! Iure voluptas explicabo fuga sunt labore voluptatibus ullam consequuntur ea, quisquam consequatur tenetur iste! Eos quod libero eveniet minima vel cupiditate animi impedit tempora recusandae, possimus iste facilis dolorem excepturi ipsam in delectus numquam quos iure earum aliquid quibusdam inventore illum pariatur repellendus? Qui possimus reiciendis aliquid, asperiores dolore incidunt amet repudiandae quia eaque quisquam eligendi iste repellat deleniti voluptatibus a commodi voluptate corrupti hic? Aperiam consequatur eveniet laboriosam veritatis, saepe minima, laudantium tempora aliquam nostrum provident sed aspernatur nisi? Quibusdam ratione soluta impedit harum libero quam recusandae eaque, reprehenderit obcaecati magni iure labore unde nobis aperiam distinctio perferendis est nulla, totam ipsam aliquid consequatur voluptas sed cupiditate. Molestias nisi error blanditiis cum inventore delectus debitis quia labore nostrum ullam accusantium modi qui, id aliquid repudiandae magni aperiam officiis fugit deserunt unde quaerat. Earum, aut? Obcaecati delectus eos voluptates optio iste amet modi distinctio harum voluptate excepturi fugiat debitis similique incidunt sapiente dicta vel maxime at enim, sunt adipisci aut vitae repellat? Dolores nostrum, obcaecati necessitatibus est asperiores dolorum repellendus numquam modi voluptatum nemo voluptatibus maxime, dolore impedit iste porro eveniet exercitationem quaerat. Vitae saepe quasi cumque necessitatibus alias officia corrupti suscipit ducimus quae magni. Commodi molestiae vel rem temporibus recusandae sit, vero doloribus earum cupiditate est odit veritatis iusto quidem tempore asperiores illum tempora, corrupti quos doloremque hic placeat eaque minus consectetur? Itaque quidem nostrum odit reiciendis ab consequuntur asperiores aperiam magni dolor eveniet odio eos quibusdam aliquid veritatis non modi excepturi dolorem deserunt iure explicabo, perferendis, quo quos blanditiis praesentium. Laborum blanditiis laudantium quae sapiente voluptatum nam a explicabo eius molestias nihil repudiandae quod ipsa aliquam rerum sint voluptates ipsum fugiat quasi, inventore dolore perferendis quia mollitia? Delectus a exercitationem nemo aliquid sed at facilis omnis cupiditate repellat laborum, temporibus placeat neque reiciendis maxime esse ex suscipit corrupti tenetur doloremque quo assumenda commodi debitis porro? Sed, amet cum. Expedita, deserunt officiis. Minus, ex maxime explicabo deserunt quia excepturi placeat in consequatur doloremque natus corrupti vero dicta reiciendis recusandae sequi est cupiditate magnam laudantium facere accusantium blanditiis quam. Similique eum rerum aut ipsum deserunt explicabo accusantium animi laborum expedita, veritatis atque impedit obcaecati sequi possimus non quod aliquam fugit minus nostrum iste quasi facilis asperiores blanditiis provident! Ex, sint, esse obcaecati commodi aliquam ullam assumenda possimus expedita repudiandae doloribus dolorem incidunt eum cum nobis sapiente in, reiciendis laboriosam cupiditate cumque iure corrupti excepturi ipsum natus ratione? Repellat impedit voluptatem, qui necessitatibus ex vitae magni, praesentium rem dolores aperiam odio. Ullam possimus itaque voluptatem id aut, ipsum tenetur impedit modi earum laboriosam, doloremque commodi porro, facere rerum ipsam pariatur odit? Eaque pariatur asperiores dolores natus accusantium laborum commodi hic, culpa illum, voluptas incidunt ea sequi maxime adipisci est necessitatibus blanditiis id doloremque. Consequatur amet fugit voluptate, unde molestiae aut harum consequuntur blanditiis doloribus repellendus dolor ratione laboriosam doloremque dolores tempore porro, maxime, aperiam exercitationem vero quae voluptatibus eum totam illo ut! Impedit, dolores. Quaerat fugiat cum aliquid, culpa nam adipisci quibusdam, modi nemo nesciunt beatae consequuntur omnis molestiae tenetur? Nobis laboriosam aliquam repellat temporibus maiores unde, quas harum ipsa iure repellendus aspernatur, tempora laborum maxime porro culpa magnam ab quos fugit dignissimos explicabo beatae voluptas, rem nihil. Est debitis quae commodi! Veniam vero consequatur ad voluptatem minima, omnis sint dolorem in amet. Deserunt commodi asperiores porro molestiae explicabo voluptatum alias voluptatem consequuntur modi laborum, iure nesciunt quidem cumque.'
      const container = document.getElementById('centerDiv');
      container.replaceChildren();

      const p = document.createElement('p');
      p.textContent = this.whatWeDo;
      const h2 = document.createElement('h2');
      h2.textContent = 'Czym się zajmujemy';
      h2.classList.add('centerDivHeader');
      container.append(h2, p);
    },
    showMembers() {
      this.members = 'Jan1, Jan2, Jan3, Jan4, Jan5, Jan6, Jan7, Jan8, Jan9, Jan10'
      const container = document.getElementById('centerDiv');
      container.replaceChildren();
      
      const p = document.createElement('p');
      p.textContent = this.members;
      const h2 = document.createElement('h2');
      h2.textContent = 'Członkowie';
      h2.classList.add('centerDivHeader');
      container.append(h2, p);
    },
    showContact() {
      this.contact = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor. Być może stworzymy projekt dla Ciebie!'
      const container = document.getElementById('centerDiv');
      container.replaceChildren();
      
      const p = document.createElement('p');
      p.textContent = this.contact;
      const h2 = document.createElement('h2');
      h2.textContent = 'Kontakt';
      h2.classList.add('centerDivHeader');
      const br = document.createElement('br');
      //const div = document.createElement('div');
      //div.classList.add('div-email');
      // const button = document.createElement('button');
      // button.textContent = 'WYŚLIJ EMAILA';
      // button.classList.add('btn-email');
      // div.appendChild(button);
      // container.append(h2, p, br, div);
      const pop = document.createElement('div');
      pop.onclick = "showPopup";
      pop.textContent = "WYŚLIJ EMAILA";
      pop.classList.add('popup'); 
      const popContent = document.createElement('span');
      popContent.textContent = "Formularz";
      popContent.classList.add("popuptext");
      pop.appendChild(popContent);
      container.append(h2, p, br, pop);
      // innerHtml
    },
    showPopup() {
      //const div = document.createElement('div');
      //Popup
      var popContent = document.getElementsByClassName("popuptext");
      popContent.classList.toggle("show");
    }
  }
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  margin: 0 auto;
} 

.title {
  /* padding-bottom: 8px; 
  text-decoration: none; */
  text-align: center;
  /* color: #333;
  font-size: 2.15rem;
  font-weight: 650; 
  line-height: 1.125; */
}

#title {
  line-height: 1.6;
  margin-bottom: 0px;
}

.p-category {
  text-align: center;
  font-size: 16px;
  color: grey;
}

#btn {
  position: relative;
  justify-content: center;
  margin-bottom: 8px;
  width: 100%;
  justify-content: left;
  color: black;
  background-color: rgb(165, 232, 163);
}

#menu {
  padding: 10px;
}

#divLinks {
  height: 100%;
  right: 0;
  width: 13%;
  min-width: 100px;
  background-color: rgb(203, 203, 203);
}

#centerDiv {
  margin-right: 15px;
  border: 5px solid rgb(203, 203, 203);
}

.btn-email {
  width: 50%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: .3s;
}

.btn-email:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

.div-email {
  display: flex;
  justify-content: center;
}

.centerDivHeader {
  padding-left: 10px;
  padding-bottom: 10px;
  font-size: 1.5rem !important;
  line-height: 1.2;
  
}

@media screen and (min-width: 1408px) {
.container:not(.is-max-desktop):not(.is-max-widescreen) {
    max-width: 1644px !important;
}
}


.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* The actual popup (appears on top) */
.popup .popuptext {
  visibility: hidden;
  width: 160px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px 0;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -80px;
}

/* Popup arrow */
.popup .popuptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

/* Toggle this class when clicking on the popup container (hide and show the popup) */
.popup .show {
  visibility: visible;
  -webkit-animation: fadeIn 1s;
  animation: fadeIn 1s;
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity:1 ;}
}

</style>