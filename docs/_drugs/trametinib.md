---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 894
evidence_level: L5
indication_count: 5
---

# Trametinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Trametinib：從轉移性黑色素瘤到非皮膚性黑色素瘤

## 一句話總結

Trametinib 是一種 MEK 抑制劑，原本用於治療轉移性黑色素瘤。
TxGNN 模型預測排名最高的新適應症為脈絡膜缺失症，但該預測缺乏生物學依據。本報告以證據最充分的**非皮膚性黑色素瘤 (Non-cutaneous Melanoma)** 為主要評估對象，目前有 **10 個臨床試驗**，但尚無直接針對該族群的文獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性黑色素瘤（許可證資料未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 非皮膚性黑色素瘤 (Non-cutaneous Melanoma) |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L2（有已完成的 Phase 2 試驗，但規模很小，且多為混合族群） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 分數排名第 1 的是脈絡膜缺失症 (Choroideremia, 99.31%)。此疾病為 X 染色體連鎖視網膜退化，由 CHM (REP1) 基因缺失引起，與 MAPK 路徑過度活化無關，也沒有任何試驗或文獻支持，分數很可能是網路傳播造成的假象，建議 Hold。因此本報告改以排名第 2、證據較充分的非皮膚性黑色素瘤為主軸。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位未收錄）。不過，藥理資料顯示 trametinib 的標的是 MEK1 (MAP2K1) 與 MEK2 (MAP2K2)，位於 BRAF/NRAS 下游的 MAPK 訊號路徑。此路徑在黑色素瘤中經常被活化，這也是 trametinib 用於 BRAF V600 突變黑色素瘤的基礎。

非皮膚性黑色素瘤（黏膜、肢端、葡萄膜等）與原適應症同屬黑色素瘤，但生物學特性差異大。帶有 BRAF V600 突變的腫瘤，理論上可能對 dabrafenib 合併 trametinib 有反應；葡萄膜黑色素瘤主要由 GNAQ/GNA11 驅動，機轉依據較弱。

現有 Phase 2 試驗多收納混合或不限腫瘤類型的族群，無法確認特定亞型的療效，也沒有 Phase 3 RCT。因此這個預測在機轉上合理，但需要亞型專屬的證據驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02296112](https://clinicaltrials.gov/study/NCT02296112) | Phase 2 | 完成 | 9 | Trametinib 用於 BRAF 非 V600 突變黑色素瘤；樣本極小，統計檢定力有限 |
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Phase 2 | 進行中（不招募） | 44 | NCI-MATCH H 組：dabrafenib + trametinib 用於 BRAF V600 突變腫瘤（不限腫瘤類型），黑色素瘤訊號為間接 |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | N/A | 完成 | 232 | 輔助性 dabrafenib + trametinib 在黑色素瘤的真實世界使用觀察研究；非皮膚性亞型占比不明 |
| [NCT05907304](https://clinicaltrials.gov/study/NCT05907304) | Phase 1 | 進行中（不招募） | 86 | Naporafenib + trametinib 用於 RAS Q61X 突變實體瘤；機轉相符，尚無結果 |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Phase 1/2 | 完成 | 74 | BGB324 合併 pembrolizumab 或 dabrafenib/trametinib；無法區分 trametinib 的貢獻 |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Phase 2 | 終止 | 10 | BRAF 突變轉移性黑色素瘤的標靶治療最佳化；樣本小、可用證據有限 |
| [NCT02974725](https://clinicaltrials.gov/study/NCT02974725) | Phase 1 | 終止 | 241 | LXH254 相關組合（含 trametinib）用於 NSCLC 或 NRAS 突變黑色素瘤；早期且已終止 |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | 招募中 | 100 | 長期安全性延伸試驗，未提供新的療效證據 |
| [NCT02416232](https://clinicaltrials.gov/study/NCT02416232) | N/A | 已不可用 | — | Trametinib 用於 BRAF V600E/K 突變皮膚黑色素瘤的擴展使用研究；無療效終點 |
| [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) | Phase 2/3 | 招募中 | 30 | DETERMINE 平台試驗：dabrafenib + trametinib 用於 BRAF V600 突變癌症，預計 2026-04 開始 |

另有 NCT05275374（XP-102 合併 trametinib，Phase 1/2，尚未招募）屬前瞻性試驗，目前無資料，未列入上表。

---

## 文獻證據

非皮膚性黑色素瘤目前無相關文獻。

與其他預測新適應症相關的文獻僅有病例報告：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | 病例報告＋文獻回顧 | Clin Exp Dermatol | 兩例 BRAF 突變結膜黑色素瘤（上皮樣細胞型），其中一例使用 vemurafenib 治療轉移；支持眼部黑色素瘤中 BRAF 標靶治療的合理性（對應眼瞼黑色素瘤、上皮樣細胞黑色素瘤） |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | 病例報告＋文獻回顧 | J Investig Med High Impact Case Rep | 日本 15 例淚囊黑色素瘤回顧，病理為大型上皮樣細胞 |
| [42583475](https://pubmed.ncbi.nlm.nih.gov/42583475/) | 2026 | 病例報告 | Ann Med Surg | 無已知原發病灶的早期轉移性 BRAF V600E 突變黑色素瘤 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64520 | MEKINIST TABLETS 0.5MG | — | 資料未載明 |
| HK-64521 | MEKINIST TABLETS 2MG | — | 資料未載明 |

兩張許可證皆為單方、有效，持有者為 Novartis Pharmaceuticals (HK) Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（MEK 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 15 筆藥物交互作用，等級皆為中度，包括：
  - Dabrafenib、Encorafenib（BRAF 抑制劑）
  - Enzalutamide、Apalutamide
  - Brigatinib、Erdafitinib、Gilteritinib、Idelalisib、Tucatinib、Midostaurin
  - Fostamatinib、Elagolix、Isavuconazonium、Lasmiditan、Sarecycline
- 另有藥理資料指出 trametinib 的作用標的為 MEK1 與 MEK2。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對非皮膚性黑色素瘤）

**理由：**
- MEK 抑制劑在 BRAF 突變黑色素瘤中有明確機轉，且已有已完成的 Phase 2 試驗，但規模小（n=9），且多為混合族群，無法確認非皮膚性亞型的療效。
- 其他預測適應症的建議：脈絡膜缺失症與陰囊黑色素瘤為 Hold；上皮樣細胞黑色素瘤與眼瞼黑色素瘤僅有病例報告，列為研究問題 (Research Question)。

**若要推進需要：**
- 依亞型（黏膜、肢端、葡萄膜）及 BRAF/NRAS/GNAQ 突變狀態分層的療效資料
- 以非皮膚性黑色素瘤為主體的 Phase 2/3 試驗，並限定 BRAF V600 突變族群
- 完整的作用機轉資料與香港仿單的警語、禁忌症
- 與 BRAF 抑制劑等併用藥物的交互作用監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

