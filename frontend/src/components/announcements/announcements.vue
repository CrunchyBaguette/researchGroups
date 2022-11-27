<template>
  <div id="content">
    <p class="title" id="tit">Ogłoszenia</p>

    <div id="announcements">
      <div class="card text-center m-3">
          <h3 class="card-header">Vue.js Pagination Tutorial & Example</h3>
          <div class="card-body">
              <div v-for="item in pageOfItems" :key="item">{{item}}</div>
              <div>
                <announcement
                id="a1"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a2"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a3"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a4"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a5"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a6"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a7"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a8"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a9"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a10"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a11"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"
                />
                <announcement
                id="a12"
                :author="annAuthor"
                :category="annCategory"
                :date="annDate" sortable
                :title="annTitle"
                :content="annContent"/>
              </div> 
          </div>
          <div class="card-footer pb-0 pt-3">
              <jw-pagination :items="exampleItems" @changePage="onChangePage"></jw-pagination>
          </div>  
      </div>

      
    </div>
  </div>
</template>

<script>
import announcement from "./announcement.vue";

// an example array of items to be paged
const exampleItems = [document.getElementById('a1'), document.getElementById('a2'), document.getElementById('a3'), 
document.getElementById('a4'), document.getElementById('a5'), document.getElementById('a6'), document.getElementById('a7'),
document.getElementById('a8'), document.getElementById('a9'), document.getElementById('a10'), document.getElementById('a11'), 
document.getElementById('a12')].map(i => ({ id: (i+1)}));
//const exampleItems = [...Array(150).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));

export default {
  name: "announcements",
  components: {
    announcement,
  }, 
  data() {
      return {
          exampleItems,
          pageOfItems: [],
          annAuthor: 'Jan Kowalski',
          annCategory: 'Poszukiwanie sponsora',
          annDate: '12.08.2022r. 17:20',
          annTitle: 'Poszukiwany inwestor',
          annContent: 'Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore. Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore.',
      };
  },
  methods: {
      onChangePage(pageOfItems) {
          // update page of items
          this.pageOfItems = pageOfItems;
      }
  }
};
</script>

<style>
.title {
  padding: 10px;
  font-size: 40px;
}

#tit {
  text-align: left;
}

#announcements {
  width: 100%;
  height: 90%;
  background-color: white;
  overflow: auto;
}

</style>

