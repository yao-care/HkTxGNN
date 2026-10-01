---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 5
---

# Everolimus
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

# Everolimus：從原核准適應症到脂肪肉瘤 (Liposarcoma)

## 一句話總結

Everolimus 是 mTOR 抑制劑，在香港已有 14 張許可證，但資料中未載明原適應症。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效。
目前**無已登記的臨床試驗**，只有 **4 篇文獻**，其中 1 篇是 Phase II 試驗報告（合併 ribociclib，僅限去分化亞型）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L3（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

**證據等級說明：** 原始資料標為 L2，但 L2 需要已完成的 Phase 2/3 RCT。目前唯一的 Phase II 試驗看起來是單臂、合併用藥設計，而且沒有臨床試驗登記紀錄。再加上有人類腫瘤組織的轉譯研究，本報告判定為 L3。

## 為什麼這個預測合理？

Everolimus 抑制 mTORC1。已有研究在去分化脂肪肉瘤 (DDLS) 中觀察到 Akt-mTOR 與 MAPK 路徑活化（PMID 26518767，99 例檢體），因此在標靶上有合理依據。

去分化脂肪肉瘤常由 CDK4/MDM2 擴增驅動。SAR-096 Phase II 試驗把 everolimus 與 CDK4/6 抑制劑 ribociclib 合併，用於晚期去分化脂肪肉瘤與平滑肌肉瘤。兩藥在多種腫瘤模型中有協同抑制生長的作用。

要注意的是，「脂肪肉瘤」包含多種亞型，現有證據只針對**去分化亞型**，不能直接推論到其他亞型。另外，目前缺乏詳細的 DrugBank 作用機轉資料，上述機轉推論來自文獻。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II 試驗（單臂，合併用藥） | Clin Cancer Res | SAR-096：ribociclib 合併 everolimus 用於晚期去分化脂肪肉瘤與平滑肌肉瘤 |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | 轉譯研究 | Tumour Biol | 99 例去分化脂肪肉瘤檢體中觀察到 Akt-mTOR 與 MAPK 路徑活化，並有 mTOR 抑制劑的體外抗腫瘤試驗 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 以 PDOX 小鼠模型尋找 palbociclib 的有效組合療法（間接相關，非 everolimus 專屬） |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 前臨床 | Anticancer Res | Eribulin 與不同機轉抗癌藥合併的前臨床活性（間接相關） |

## 香港上市資訊

共 14 張許可證，以下列出 5 張。資料中未提供核准適應症文字與劑型欄位。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-59060 | AFINITOR TAB 5MG | Novartis Pharmaceuticals (HK) Limited |
| HK-61710 | AFINITOR TABLETS 2.5MG | Novartis Pharmaceuticals (HK) Limited |
| HK-54335 | CERTICAN TAB 0.5MG | Novartis Pharmaceuticals (HK) Limited |
| HK-68855 | EVEROLIMUS TEVA TABLETS 5MG | Teva Pharmaceutical Hong Kong Limited |
| HK-68853 | EVEROLIMUS TEVA TABLETS 10MG | Teva Pharmaceutical Hong Kong Limited |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據只有一項單臂 Phase II 試驗與若干轉譯及前臨床研究，且僅涵蓋去分化亞型，尚無已登記試驗或 RCT。
- 香港仿單的警語與禁忌資料尚未取得，是阻斷性資料缺口，無法進入安全性篩選。

TxGNN 預測的其他適應症（卵巢黏液樣脂肪肉瘤、隆突性皮膚纖維肉瘤、副腦膜胚胎型橫紋肌肉瘤、陰道葡萄狀胚胎型橫紋肌肉瘤）均無 everolimus 專屬證據，維持 Hold。

**若要推進需要：**
- 下載並解析香港衛生署的仿單，取得警語與禁忌症。
- 補齊 DrugBank 的作用機轉與藥物交互作用資料。
- 追蹤 SAR-096 的完整結果，並確認是否有已登記的臨床試驗。
- 釐清 everolimus 對各脂肪肉瘤亞型（特別是非去分化型）的適用性。
- 補上各許可證的核准適應症，確認原適應症。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

