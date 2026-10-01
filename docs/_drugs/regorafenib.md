---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Regorafenib：從大腸直腸癌到脂肪肉瘤

## 一句話總結

Regorafenib 是口服多激酶抑制劑，文獻記載它原本用於治療轉移性大腸直腸癌與胃腸道基質瘤 (GIST)。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，目前有 **2 個臨床試驗**和 **9 篇文獻**可供參考。
但這些隨機對照試驗的結果**並不支持**脂肪肉瘤這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L2（有已完成的 Phase 2 RCT，但脂肪肉瘤世代結果為陰性） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Regorafenib 是多激酶抑制劑，標靶包括血管新生相關激酶 (VEGFR1-3、TIE2)、基質激酶 (PDGFR-β、FGFR) 和致癌受體酪胺酸激酶 (KIT、RET、RAF)。DrugBank 的作用機轉欄位目前沒有資料，以上描述來自文獻回顧。

抗血管新生與基質激酶阻斷，在軟組織肉瘤中有合理的理論基礎。同類藥物 pazopanib 已用於非脂肪細胞型軟組織肉瘤，regorafenib 也曾在這類肉瘤中顯示療效。因此模型預測它對脂肪肉瘤有效，從機轉上看並非沒有道理。

不過，脂肪肉瘤在生物學上自成一類。高分化與去分化亞型的特徵是 MDM2/CDK4 擴增，與其他軟組織肉瘤的驅動機制不同。REGOSARC 試驗顯示，regorafenib 對平滑肌肉瘤、滑膜肉瘤和其他非脂肪細胞型肉瘤有效，**對脂肪肉瘤則無效**。0.998 的 TxGNN 分數只是模型預測，不能取代臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | 完成 | 219 | REGOSARC：多國隨機、雙盲、安慰劑對照，用於曾接受 anthracycline 治療的轉移性軟組織肉瘤，設有脂肪肉瘤世代。療效主要出現在其他亞型 |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | SARC024：針對特定肉瘤亞型（含脂肪肉瘤世代）的 blanket protocol，設計部分為非比較性，世代規模小 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC 主要報告：評估 regorafenib 用於曾接受 anthracycline 治療的轉移性軟組織肉瘤的療效與安全性 |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | REGOSARC 更新分析：對平滑肌肉瘤、滑膜肉瘤等非脂肪細胞型肉瘤有效，**對脂肪肉瘤無效** |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 脂肪肉瘤世代：結果與先前資料一致，**不支持**在此族群常規使用 regorafenib |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT 事後分析 | Cancer | REGOSARC 的 Q-TWiST 探索性分析，評估臨床獲益（針對非脂肪細胞型肉瘤） |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | 回顧 regorafenib 在肉瘤治療中日益重要的角色，指出療效依組織亞型而異 |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | 晚期軟組織肉瘤一線治療後的維持療法回顧 |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | 試驗計畫書 | BMC Cancer | REGOSARC 試驗設計說明 |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | 回溯性研究（間接） | Anti-Cancer Drugs | 研究藥物為 anlotinib，用於無法切除或轉移性高分化／去分化脂肪肉瘤，非 regorafenib |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | 個案報告（間接） | Rare Tumors | pazopanib 用於 Ewing 肉瘤，為 SARC024 增設 Ewing 肉瘤世代提供依據，與脂肪肉瘤無直接關係 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63304 | STIVARGA TAB 40MG | BAYER HEALTHCARE LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多激酶抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 低（依藥物類別判斷） |
| 監測項目 | 肝功能、血壓、皮膚（手足皮膚反應）；血液學參數請依仿單 |
| 處置防護 | 請參考原廠仿單及機構的抗腫瘤藥物處置規範 |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻提到，這類抗血管新生多激酶抑制劑常見的不良反應包括手足皮膚反應、高血壓、腹瀉、疲倦與肝毒性。這些是文獻層級的描述，不能取代香港衛生署核准的仿單內容。

## 結論與下一步

**決策：Hold**

**理由：**
脂肪肉瘤有 2 個已完成的 Phase 2 試驗，但 REGOSARC 與 SARC024 的脂肪肉瘤世代都未顯示療效，SARC024 作者更明確表示不支持常規使用。這個高分預測目前被實際臨床證據否定，不宜推進。

**若要推進需要：**
- 從 REGOSARC 與 SARC024 的原始論文確認脂肪肉瘤世代的 PFS 與反應率數據，並依亞型（高分化／去分化、黏液樣、多形性）分層檢視
- 取得香港衛生署仿單的警語與禁忌資料，這是目前進入安全性篩選的阻礙
- 補齊 DrugBank 作用機轉資料
- 考慮組合治療策略（SARC024 作者建議探索）
- 另一個值得追蹤的方向是**腎細胞癌**。透明細胞腎細胞癌（預測排名第 3）與一般腎細胞癌（排名第 10）的證據等級為 L3，有單臂 Phase 2 與前臨床資料，但目前尚無隨機對照證據，且需與既有 VEGFR-TKI 及免疫檢查點抑制劑組合比較。其餘 7 項預測目前僅有模型分數，應維持 Hold。

本報告僅供研究參考，不構成醫療建議；老藥新用候選須經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

