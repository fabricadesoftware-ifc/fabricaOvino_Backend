<template>
  <div class="category-admin">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.category.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>

    <section class="section is-main-section">
      <card-component title="Adicionar / Editar" icon="ballot">
        <form-category v-model="category" />
      </card-component>
      <hr />
      <card-component
        class="has-table has-mobile-sort-spaced"
        title="Categorias"
        icon="alpha-c-circle-outline"
      >
        <list-category @loadCategory="loadCategory" />
      </card-component>
    </section>
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import FormCategory from '@/components/categories/FormCategory'
import ListCategory from '@/components/categories/ListCategory'

export default {
  components: { FormCategory, ListCategory, CardComponent, HeroBar, TitleBar },
  data: function () {
    return {
      category: {}
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.category.title')]
    }
  },
  methods: {
    loadCategory(category) {
      this.category = {
        id: category.id,
        name: category.name
      }
    }
  }
}
</script>
