<template>
  <div class="category-admin">
    <PageTitle
      icon="alpha-c-circle-outline"
      :main="$t('pages.admin.category.title')"
      :sub="$t('pages.admin.category.subtitle')"
    />
    <form-category v-model="category" />
    <hr />
    <list-category @loadCategory="loadCategory" />
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import FormCategory from '@/components/categories/FormCategory'
import ListCategory from '@/components/categories/ListCategory'

export default {
  components: { FormCategory, ListCategory, PageTitle },
  data: function () {
    return {
      category: {}
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
