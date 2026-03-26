---
layout: home
title: HkTxGNN - 香港老藥新用預測系統
---

# HkTxGNN - 香港老藥新用預測系統

基於 [TxGNN](https://github.com/mims-harvard/TxGNN) 知識圖譜的香港藥品老藥新用預測系統。

## 系統概覽

| 項目 | 數值 |
|------|------|
| 香港註冊藥品 | 14,252 |
| DrugBank 映射成功 | 1,261 |
| 映射率 | 82% |
| 候選配對數 | 21,513,581 |

## 資料來源

- **藥品資料**：[香港藥物辦公室](https://www.drugoffice.gov.hk/)
- **知識圖譜**：[TxGNN](https://github.com/mims-harvard/TxGNN) (Harvard MIMS Lab)
- **藥物識別**：[DrugBank](https://www.drugbank.com/)

## FHIR API

本系統提供 FHIR R4 相容的 API：

- [CapabilityStatement](/fhir/metadata)
- [MedicationKnowledge](/fhir/MedicationKnowledge/)
- [ClinicalUseDefinition](/fhir/ClinicalUseDefinition/)

## SMART on FHIR

支援 SMART on FHIR 整合：

- [SMART Launch](/smart/launch.html)

## 免責聲明

⚠️ **重要提示**：本系統的預測結果僅供研究參考，不構成醫療建議。
老藥新用候選需經過嚴格的臨床驗證才能應用於臨床實踐。
使用者應諮詢專業醫療人員以獲得適當的醫療建議。

## 專案資訊

- **GitHub**: [yao-care/HkTxGNN](https://github.com/yao-care/HkTxGNN)
- **開發者**: [Yao.Care](https://yao.care)
- **授權**: MIT License

---

© 2026 Yao.Care. All rights reserved.
