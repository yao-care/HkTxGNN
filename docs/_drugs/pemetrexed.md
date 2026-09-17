---
layout: default
title: Pemetrexed
parent: 高證據等級 (L1-L2)
nav_order: 569
evidence_level: L2
indication_count: 5
---

# Pemetrexed
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# PEMETREXED：從惡性胸膜間皮瘤到惡性腹膜間皮瘤

## 一句話總結

Pemetrexed（DB00642）是一種多標靶抗葉酸化療藥物，原為惡性胸膜間皮瘤（malignant pleural mesothelioma）及非小細胞肺癌之標準用藥。TxGNN 模型預測它可能對**惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma)** 有效，目前有 **11 個臨床試驗**和 **20 篇文獻**支持這個方向，機轉上與已核准的胸膜間皮瘤適應症具高度延伸性。

> 補充說明：本次證據包同時預測了 5 個間皮瘤相關適應症，其中「惡性胸膜間皮瘤」（rank 3）與「胸膜上皮樣間皮瘤」（rank 4）證據等級達 **L1**（已有完成的 Phase 3 RCT），強度高於本報告主要聚焦的腹膜間皮瘤（L2）。詳見文末備註。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma) |
| TxGNN 預測分數 | 99.99%（排名第 330） |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Pemetrexed 是多標靶抗葉酸藥物，抑制胸苷酸合成酶（TS）、雙氫葉酸還原酶（DHFR）及甘胺醯胺核苷酸甲醯轉移酶（GARFT），阻斷 DNA 合成所需的胸苷酸與嘌呤核苷酸生合成，屬於廣效性細胞毒殺機轉。

這個機轉與腫瘤的組織來源（間皮細胞）而非解剖部位相關，因此對胸膜與腹膜間皮瘤具有相同的細胞毒性基礎。事實上，Pemetrexed 併用 cisplatin 已是惡性胸膜間皮瘤的 FDA/EMA 核准標準一線治療（1998 年 EMPHACIS Phase III 試驗確立），而腹膜間皮瘤在臨床實務上長期依循相同的 pemetrexed-platinum 骨幹用藥，僅缺乏腹膜部位專屬的大型 RCT 驗證。

換言之，TxGNN 的預測並非憑空推論，而是反映了間皮瘤這一疾病譜系中，已在胸膜亞型驗證的機轉延伸到腹膜亞型的臨床實作慣例。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | 招募中 | 66 | 隨機分派比較 carboplatin+pemetrexed+bevacizumab ± atezolizumab（免疫治療）於腹膜間皮瘤 |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | 完成 | 48 | ALIMTA（pemetrexed）+gemcitabine 一線治療胸膜或腹膜間皮瘤，已完成 |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | 招募中 | 64 | ICARuS II：CRS+HIPEC 術後比較腹腔內化療 vs 靜脈化療 |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | 狀態未知 | 40 | 一線鉑類化療後 talazoparib 維持治療，涵蓋胸膜/腹膜間皮瘤三世代族群 |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | 進行中（未招募） | 30 | TRC102 併用 cisplatin+pemetrexed，治療晚期實體瘤及難治性間皮瘤 |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | 已終止 | 85 | ADI-PEG20 併用 pemetrexed+cisplatin，已終止 |
| [NCT03564691](https://clinicaltrials.gov/study/NCT03564691) | Phase 1 | 完成 | 470 | MK-4830 單藥/併用 pembrolizumab，多癌別籃式試驗，非疾病特異 |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | 已撤回 | 0 | Vorinostat 併用 pemetrexed-cisplatin 一線治療胸膜間皮瘤，未實際執行 |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | 招募中 | 28 | Sintilimab+bevacizumab 併用 pemetrexed+cisplatin，治療不可切除腹膜間皮瘤 |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | 暫停 | 66 | MESOTIP：PIPAC 併全身化療 vs 全身化療單獨，作為腹膜間皮瘤一線治療（已暫停） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and peritoneum | 雙向化療（BDC）提升初始不可切除腹膜間皮瘤之可切除性 |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | 回顧性研究 | Expert Rev Anticancer Ther | 評估 pemetrexed+cisplatin 一線全身治療於腹膜間皮瘤之療效 |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | 回顧性研究 | Jpn J Clin Oncol | 評估 cisplatin+pemetrexed 作為晚期腹膜間皮瘤一線治療之療效與安全性 |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | 多中心研究 | Ann Surg Oncol | 分析腹膜間皮瘤族群之人口學、臨床病理特徵與治療選擇 |
| [35765009](https://pubmed.ncbi.nlm.nih.gov/35765009/) | 2022 | 回顧性研究 | World J Surg Oncol | 分析 52 名女性腹膜間皮瘤病患之預後因子 |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | 病例報告 | BMJ Case Reports | 腹膜間皮瘤病患對 cisplatin+pemetrexed 再挑戰治療反應良好，附文獻回顧 |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | 病例系列 | J Immunother | 2 例鉑類無反應之轉移性腹膜間皮瘤病患接受化學免疫治療之臨床病程 |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | 病例報告 | BMJ Case Reports | Nivolumab 治療腹膜間皮瘤之病例報告 |
| [22104079](https://pubmed.ncbi.nlm.nih.gov/22104079/) | 2012 | Review | Cancer Treat Rev | 彌漫性腹膜間皮瘤治療進展回顧 |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | 腹膜間皮瘤病患治療方式綜述 |

---

## 細胞毒性

Pemetrexed 屬已上市多年的細胞毒殺性化療藥物（抗葉酸類），以下為此藥物類別之一般已知風險；本證據包未提供 TFDA/香港仿單之量化毒性數據，實際處置仍請以官方仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（多標靶抗葉酸藥物，Antifolate） |
| 骨髓抑制風險 | 高（常見嗜中性白血球減少、貧血、血小板減少；臨床上需併用葉酸與維生素 B12 以降低血液毒性） |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含白血球分類）、肝腎功能、肌酸酐清除率（腎功能不良會顯著增加毒性風險） |
| 處置防護 | 需依細胞毒性藥物處置規範操作（配製、給藥、廢棄均應遵循危害性藥物處理程序） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個 Phase 2 RCT（NCT05001880）及多項直接相關的腹膜間皮瘤治療試驗/世代研究支持 pemetrexed 骨幹化療的應用，且其抗葉酸機轉已在同源疾病（胸膜間皮瘤）中透過 Phase III RCT 明確驗證，跨解剖部位延伸具合理性。
- 但腹膜間皮瘤本身仍屬罕見疾病，目前無專屬完成之 Phase 3 RCT，證據等級僅達 L2，需審慎管理臨床期待。

**若要推進需要：**
- 補齊 TFDA／香港仿單警語與禁忌症資料（DG001，Blocking，目前無法進行 S1 安全性初評）
- 確認詳細作用機轉（MOA）之官方來源資料（DG002）
- 確認香港上市與許可證狀態（現況：未上市，0 張許可證）
- 比較同批預測中證據更強的候選適應症（惡性胸膜間皮瘤 L1／胸膜上皮樣間皮瘤 L1），評估是否優先推進整體「間皮瘤」適應症擴增策略，而非單獨聚焦腹膜亞型
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

