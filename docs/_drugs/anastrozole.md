---
layout: default
title: Anastrozole
parent: 高證據等級 (L1-L2)
nav_order: 60
evidence_level: L1
indication_count: 10
---

# Anastrozole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Anastrozole：預測適應症為女性乳癌（既有用途的模型驗證）

## 一句話總結

Anastrozole 是非類固醇類芳香環轉化酶抑制劑，資料包未記載原適應症，但它在停經後荷爾蒙受體陽性乳癌的用途早已確立。
TxGNN 預測它對**女性乳癌 (female breast carcinoma)** 有效，這與既有用途相符，可視為模型的正向對照。
目前有 **50 個臨床試驗**和 **20 篇文獻**支持，其中包含多個已完成的大型 Phase 3 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (female breast carcinoma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據評估內容，Anastrozole 是非類固醇類芳香環轉化酶抑制劑。它降低停經後女性周邊組織的雌激素合成，從而抑制荷爾蒙受體陽性乳癌腫瘤的生長。

這個預測與已知機轉一致，高分（0.997）反映的是既有適應症，而不是新發現。因此本案更像模型的正向對照，而非真正的老藥新用候選。資料包中原適應症欄位為空，這是資料缺口，不代表沒有既有用途。

這個結論適用於停經後、荷爾蒙受體陽性的患者。其他預測項目（如神經母細胞瘤等）並無類似的機轉支持，見結論。

## 臨床試驗證據

以下從 50 個登記試驗中，列出已完成的大型 Phase 3 與其他最相關的 10 個。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | 完成 | 9358 | 停經後乳癌輔助治療：Arimidex 單用 vs Nolvadex 單用 vs 兩者併用（ATAC 試驗） |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | 完成 | 7576 | Exemestane vs Anastrozole 用於停經後受體陽性原發性乳癌，比較預防復發效果 |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | 完成 | 4172 | Letrozole vs Anastrozole 用於荷爾蒙受體與淋巴結陽性乳癌輔助治療 |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | 完成 | 2980 | IBIS-II DCIS：Tamoxifen vs Anastrozole 用於原位乳管癌術後 |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | 完成 | 1914 | Tamoxifen 2–3 年後，比較 Anastrozole 6 年 vs 3 年的輔助治療 |
| [NCT00256698](https://clinicaltrials.gov/study/NCT00256698) | Phase 3 | 完成 | 514 | FACT：Anastrozole 單用 vs 併用 Fulvestrant，用於首次復發的受體陽性乳癌 |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | 完成 | 298 | Exemestane vs Anastrozole 作為晚期/復發乳癌初始荷爾蒙治療，驗證非劣性 |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | 完成 | 3420 | Denosumab vs 安慰劑，預防接受芳香環轉化酶抑制劑的非轉移性乳癌患者發生骨折 |
| [NCT01151215](https://clinicaltrials.gov/study/NCT01151215) | Phase 2 | 提前終止 | 482 | AZD8931 併用 Anastrozole vs Anastrozole 單用，用於晚期或轉移性乳癌（MINT） |
| [NCT04711252](https://clinicaltrials.gov/study/NCT04711252) | Phase 3 | 進行中（不再招募） | 1370 | SERENA-4：AZD9833 + Palbociclib vs Anastrozole + Palbociclib，用於晚期乳癌一線治療 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT | Lancet | IBIS-II 長期結果：Anastrozole vs 安慰劑用於預防高風險女性乳癌 |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT | Lancet | ATAC 5 年結果：Anastrozole 較 Tamoxifen 顯著延長無病存活期 |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS：雙盲試驗比較 Anastrozole 與 Tamoxifen 預防原位乳管癌術後的局部與對側乳癌 |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | 統合分析 | Oncotarget | 統合分析比較 Anastrozole 與 Tamoxifen 作為乳癌輔助治療的療效與安全性 |
| [30499075](https://pubmed.ncbi.nlm.nih.gov/30499075/) | 2020 | 統合分析 | Pathol Oncol Res | 原位乳管癌內分泌治療的統合分析，含 Tamoxifen 與 Anastrozole 的比較 |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opin Pharmacother | 比較 Anastrozole、Letrozole、Exemestane 在早期乳癌的角色 |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Review | Rev Assoc Med Bras | Anastrozole 用於乳癌化學預防與治療的文獻回顧 |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | Oncology | Anastrozole 在晚期、早期乳癌到預防的整個病程中的角色 |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | 藥物基因體學 | Clin Pharmacol Ther | 4,465 名早期乳癌患者中，SNP 基因型與 Anastrozole、Exemestane 療效的交互作用 |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | 藥物基因體學 | JCI Insight | 芳香環轉化酶抑制劑的藥物基因體學，及 Anastrozole 的其他作用機轉 |

## 香港上市資訊

香港共有 11 張許可證，以下列出 5 張主要許可證。資料中劑型與核准適應症欄位皆為空，品名顯示為 1 mg 錠劑。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-42327 | ARIMIDEX TAB 1MG | ASTRAZENECA HONG KONG LIMITED |
| HK-60845 | ANASTROZOLE TAB 1MG | KAI YUEN PHARMACEUTICAL CO |
| HK-59928 | ANASTROZOLE TAB 1MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-61332 | ANASTROZOLE STADA TAB 1MG | STADA PHARMACEUTICALS (ASIA) LIMITED |
| HK-59104 | AREMED 1 TAB 1MG | HEALTHCARE PHARMASCIENCE LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 內分泌治療藥物（芳香環轉化酶抑制劑），非傳統細胞毒性化療藥物 |

其餘細胞毒性項目（骨髓抑制、致吐性、處置防護）請參考原廠仿單的警語與注意事項。

## 安全性考量

- **需監測的風險**：骨質流失與心血管風險。多項試驗（如 denosumab 預防芳香環轉化酶抑制劑相關骨折）也在處理骨骼安全議題。
- **使用範圍**：療效僅適用於停經後、荷爾蒙受體陽性的患者。
- **肌肉骨骼副作用**：芳香環轉化酶抑制劑與肌肉骨骼及結締組織副作用有關。

警語、禁忌症與藥物交互作用資料目前查無資料，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個已完成的大型 Phase 3 隨機對照試驗（如 ATAC、MA.27、FACE、IBIS-II）支持 Anastrozole 用於乳癌，證據等級為 L1。
- 這是既有用途，並非真正的老藥新用，應搭配患者族群限制與骨骼、心血管監測。

**其他預測項目：**
排名第 2 至第 10 的預測（神經母細胞瘤、節神經母細胞瘤、單核球性白血病、橫紋肌肉瘤、骨髓性白血病等）皆為 Hold。它們缺乏機轉依據，多數沒有臨床試驗或文獻，可能是知識圖譜的假象。少數有文獻者僅為間接資料，例如乳癌轉移病例報告、奈米粒子前臨床研究，並非療效證據。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症
- 補齊 DrugBank 的作用機轉資料
- 補上各許可證的核准適應症與劑型
- 確認原適應症欄位，區分既有用途與真正新適應症

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

