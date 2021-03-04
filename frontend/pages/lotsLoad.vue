<template>
  <section>
    <PageTitle
      icon="view-grid"
      :main="$t('pages.pagetitle.lots.title')"
      :sub="$t('pages.pagetitle.lots.subtitle')"
    />
    <b-tabs>
      <b-tab-item :label="$t('asideMenu.reproductionItems.lots')"></b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
export default {
  components: { PageTitle },
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
