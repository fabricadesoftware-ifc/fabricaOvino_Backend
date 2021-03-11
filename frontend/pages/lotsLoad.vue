<template>
  <section>
    <PageTitle
      icon="view-grid"
      :main="$t('pages.pagetitle.lots.title')"
      :sub="$t('pages.pagetitle.lots.subtitle')"
    />
    <b-tabs>
      <b-tab-item
        :label="$t('pages.lots.table.title') + ': ' + lots.description"
      >
        <table-sheeps />
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import TableSheeps from '@/components/lots/TableSheeps.vue'
export default {
  components: { PageTitle, TableSheeps },
  asyncData({ params }) {
    return {
      lots: params.lots
    }
  },
  data() {
    return {
      data: {}
    }
  }
}
</script>

<style></style>
