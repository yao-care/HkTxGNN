---
layout: default
title: Selumetinib
parent: 中證據等級 (L3-L4)
nav_order: 680
evidence_level: L3
indication_count: 10
---

# Selumetinib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Selumetinib：從資料缺口的原適應症到周邊神經鞘瘤與惡性橫紋肌樣瘤等罕見腫瘤

## 一句話總結

> Selumetinib 是一款 **MEK1/2 抑制劑**，本評估包未取得其原始核准適應症與完整作用機轉資料（列為 Blocking / High 等級資料缺口）。
> TxGNN 對此藥物產出 **10 個高分（>99.9%）罕見疾病預測**，但其中 8 個僅有演算法分數、完全無臨床或文獻證據（L5，建議 Hold）。
> 僅 **周邊神經鞘瘤 (Peripheral Nerve Schwannoma)** 與 **惡性橫紋肌樣瘤 (Rhabdoid Tumor)** 有實際證據支持（L3），
> 前者有 **1 個 Phase 2 臨床試驗**（已終止）與 **7 篇文獻**（含 1 篇顯示部分反應的病例報告）。

---

## 快速總覽（以證據最充分的候選為主：周邊神經鞘瘤）

| 項目 | 內容 |
|------|------|
| 原適應症 | ⚠️ 資料缺口（本評估包 `original_indications` 為空，需另行查證原廠核准適應症） |
| 預測新適應症 | 周邊神經鞘瘤 (Peripheral Nerve Schwannoma) |
| TxGNN 預測分數 | 99.95%（全域排名 1578） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

### 十大候選適應症總覽

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|---------|-----------|---------|---------|------|
| 1 | Familial generalized lentiginosis | 99.96% | L5 | S0 | Hold |
| 2 | Gastrocutaneous syndrome | 99.96% | L5 | S0 | Hold |
| 3 | Rhabdoid tumor | 99.96% | L3 | S1 | Research Question |
| 4 | Congenital multiple café-au-lait macules syndrome | 99.96% | L5 | S0 | Hold |
| 5 | Acromelanosis | 99.96% | L5 | S0 | Hold |
| 6 | Moynahan syndrome (LEOPARD 症候群) | 99.96% | L5 | S0 | Hold |
| 7 | Leukonychia totalis-acanthosis nigricans-like lesions 症候群 | 99.95% | L5 | S0 | Hold |
| 8 | Osteopathia striata-pigmentary dermopathy 症候群 | 99.95% | L5 | S0 | Hold |
| 9 | **Peripheral nerve schwannoma** | 99.95% | **L3** | **S2** | **Research Question** |
| 10 | Trigeminal schwannoma | 99.95% | L5 | S0 | Hold |

---

## 為什麼這個預測合理？

Selumetinib 是 **MEK1/2 抑制劑**，作用於 RAS-RAF-**MEK**-ERK 訊號通路（此為評估包內各候選 rationale 中一致提及的機轉描述；官方 `original_moa` 欄位本身為資料缺口，需另行以 DrugBank 補齊）。

10 個候選中，多數屬於 **RASopathy 光譜的罕見色素性/皮膚疾病**（如 familial generalized lentiginosis、LEOPARD 症候群、café-au-lait macules 症候群等）。這類疾病理論上與 RAS/MAPK 通路過度活化有關，MEK 抑制劑在機轉上「說得通」，但**完全沒有臨床或前臨床證據**支持，屬於 TxGNN 演算法層級的推論，故均建議 Hold。

真正有實際證據支持的兩個候選：

1. **周邊神經鞘瘤（NF2 相關腫瘤）**：NF2/merlin 缺失會導致下游 RAS-RAF-MEK-ERK 通路活化，MEK 抑制劑機轉直接相關，且與已核准的 NF1 叢狀神經纖維瘤（plexiform neurofibroma）適應症生物學相近。已有疾病特異性 Phase 2 試驗（NCT03095248）及病例報告顯示部分反應（PMID 38058737）。
2. **惡性橫紋肌樣瘤（AT/RT）**：主要驅動基因為 SMARCB1 缺失，非直接 RAS/MAPK 突變，但文獻提示 LIN28-MAPK 軸參與致病（PMID 25638158），MEK 抑制劑機轉為間接/輔助性。相關臨床試驗（NCT03155620）為 basket trial 的其中一個治療臂，非疾病專屬設計。

---

## 臨床試驗證據

| 疾病 | 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|------|---------|------|------|------|---------|
| 周邊神經鞘瘤 | [NCT03095248](https://clinicaltrials.gov/study/NCT03095248) | Phase 2 | **已終止** | 10 | NF2 相關腫瘤（含 schwannoma）之 selumetinib 療效與聽力變化評估；疾病特異性試驗，但樣本量小且已終止，終止原因未載於本評估包，需查明是安全性、招募還是商業考量。 |
| 惡性橫紋肌樣瘤 | [NCT03155620](https://clinicaltrials.gov/study/NCT03155620) | Phase 2 | 進行中（未招募新病人） | 1376 | NCI-COG Pediatric MATCH 分子篩選 basket trial，selumetinib 僅為其中一個治療臂，非 rhabdoid tumor 專屬療效試驗。 |

其餘 8 個候選（familial generalized lentiginosis、gastrocutaneous syndrome 等）**目前無相關臨床試驗登記**。

---

## 文獻證據

| 疾病 | PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|-----|------|------|---------|
| 周邊神經鞘瘤 | [38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/) | 2023 | Case Report | Mol Ther Methods Clin Dev | NF2 合併 ependymoma 病人使用 selumetinib 出現部分反應（PR），為目前最直接的臨床反應證據。 |
| 周邊神經鞘瘤 | [19804833](https://pubmed.ncbi.nlm.nih.gov/19804833/) | 2010 | Preclinical | Neurobiol Dis | MEK1/2 抑制劑 AZD6244（即 selumetinib）抑制原代 schwannoma 細胞之 ERK1/2 活化與增生。 |
| 周邊神經鞘瘤 | [37046591](https://pubmed.ncbi.nlm.nih.gov/37046591/) | 2023 | Expert Consensus | Cancers | EURACAN 周邊/顱神經腫瘤診斷治療專家建議。 |
| 周邊神經鞘瘤 | [37906356](https://pubmed.ncbi.nlm.nih.gov/37906356/) | 2023 | Review | Curr Oncol Rep | NF1/NF2/schwannomatosis 中樞與周邊神經系統腫瘤治療回顧，提及 MEK 抑制劑進展。 |
| 周邊神經鞘瘤 | [38216572](https://pubmed.ncbi.nlm.nih.gov/38216572/) | 2024 | Preclinical | Nat Commun | NF1/NF2 腫瘤抑制基因交互作用導致 Schwann 細胞去分化與治療抗性之分子機制。 |
| 周邊神經鞘瘤 | [33835000](https://pubmed.ncbi.nlm.nih.gov/33835000/) | 2020 | Case Report | Acta Dermatovenerol Croat | 非 NF1 相關之叢狀神經纖維瘤病例報告。 |
| 周邊神經鞘瘤 | [40861330](https://pubmed.ncbi.nlm.nih.gov/40861330/) | 2025 | Case Report | Surg Case Rep | NF1 相關巨大縱膈腔 schwannoma 手術治療病例。 |
| 惡性橫紋肌樣瘤 | [25638158](https://pubmed.ncbi.nlm.nih.gov/25638158/) | 2015 | Preclinical | Oncotarget | 破壞 LIN28 揭示 MAPK 通路為非典型畸胎樣橫紋肌樣瘤（AT/RT）治療標的之重要性。 |

其餘 8 個候選**目前無相關文獻**。

---

## 香港上市資訊

Selumetinib 目前**未在香港取得藥物許可證**（`total_licenses = 0`），無登記資料可供列出。

---

## 細胞毒性

Selumetinib 於各候選適應症的機轉描述中被一致標註為「MEK1/2 抑制劑」，屬於標靶藥物而非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（MEK1/2 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項（本評估包無相關資料） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。
>
> 本評估包已將「TFDA 仿單警語/禁忌」列為 **Blocking 等級資料缺口（DG001）**，直接導致本藥物**無法進入 S1 安全性初評**。這是目前整個評估流程最主要的瓶頸，優先於任何適應症層級的討論。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 10 個候選中 8 個為 L5（僅演算法分數，無任何證據），不具備推進條件。
- 證據最充分的周邊神經鞘瘤候選（L3, S2）雖有疾病特異性 Phase 2 試驗與病例報告支持機轉合理性，但該試驗**已終止**且樣本數僅 10 人，終止原因不明，尚不足以支撐 Go 決策。
- 安全性初評因 Blocking 等級資料缺口（DG001）無法進行，在此缺口補齊前無法對任何候選做出最終決策。

**若要推進需要：**
- **（Blocking）** 取得 TFDA/原廠仿單警語與禁忌症資料，完成 S1 安全性初評（DG001）。
- **（High）** 透過 DrugBank API 補齊完整作用機轉（MOA）資料，以強化機轉關聯性分析（DG002）。
- 查明 NCT03095248（周邊神經鞘瘤試驗）終止原因，判斷是否為安全性訊號。
- 若聚焦周邊神經鞘瘤 / NF2 相關腫瘤方向，建議進一步蒐集其他區域註冊試驗（如 ICTRP）與最新病例系列報告，補強 L3 → L2 的證據升級路徑。
- 其餘 8 個 L5 候選建議暫不投入資源，除非未來出現前臨床或臨床證據。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

