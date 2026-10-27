---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 795
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sacubitril：預測新適應症為腦小血管病變 1 型（伴或不伴眼部異常）(brain small vessel disease 1 with or without ocu…（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "SACUBITRIL"
predicted_indications: ["brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "rheumatoid arthritis", "hemoglobinopathy"]
---

# Sacubitril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Sacubitril：從心臟衰竭相關適應症到糖尿病腎病變
{: .text-alpha }

## 一句話總結

Sacubitril 是 Entresto（沙庫巴曲／纈沙坦）的成分之一，在香港已有 9 張有效許可證。
TxGNN 模型預測排名第一的新適應症為腦小血管病變，但該預測缺乏實際證據。證據最完整的是第三順位的 **糖尿病腎病變 (Diabetic Nephropathy)**，目前有 **1 個臨床試驗**（Phase 4，狀態未知）和 **15 篇文獻**，其中多數為動物實驗與綜述。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 腦小血管病變 1 型（伴或不伴眼部異常）(brain small vessel disease 1 with or without ocular anomalies) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5（排名第一的預測）；糖尿病腎病變為 L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold（排名第一的預測）；糖尿病腎病變為 Proceed with Guardrails 的研究候選 |

> 說明：排名第一的預測缺乏任何相關證據，因此下文除了呈現前五名預測的概況外，也將證據最完整的糖尿病腎病變單獨列出。

### 前五名預測概況

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 腦小血管病變 1 型 | 99.58% | L5 | Hold |
| 2 | 常染色體顯性家族性血尿－視網膜小動脈迂曲－攣縮症候群 | 99.57% | L5 | Hold |
| 3 | 糖尿病腎病變 | 99.50% | L3 | 研究議題（Research Question） |
| 4 | 類風濕性關節炎 | 99.35% | L5 | Hold |
| 5 | 血紅蛋白病變 | 99.18% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sacubitril 是 Entresto 複方（與 valsartan 合用）的一部分，作用上為腦啡肽酶（neprilysin）抑制劑前驅藥，可提升利鈉肽濃度；valsartan 則為血管收縮素 II 第一型受體阻斷劑。

**糖尿病腎病變（證據最完整）：** 阻斷腎素－血管收縮素系統是糖尿病腎病變的治療基石。Sacubitril/valsartan 在此基礎上再增加利鈉肽作用，理論上可降低腎絲球內壓、減少蛋白尿、氧化壓力、NF-κB 介導的發炎與纖維化。多項糖尿病囓齒動物研究報告了腎臟保護效果，包括腸道菌相調節與氧化壓力下降，但在 db/db 小鼠模型中效果與 valsartan 相比有差異。

**腦小血管病變 1 型與相關症候群（排名第一、第二）：** 這兩者屬 COL4A1 相關罕見疾病，涉及基底膜缺陷與血管脆弱。預測可能源自知識圖譜中基因或路徑的鄰近關係，並無直接機轉證據。降血壓與血行動力學變化對腦血管脆弱的患者還可能帶來風險。

**類風濕性關節炎與血紅蛋白病變：** 未發現明確的機轉連結，僅為模型預測。

---

## 臨床試驗證據

以下為糖尿病腎病變（證據最完整的預測）的試驗；其他四個預測目前無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | 未知 | 297 | 比較 sacubitril/valsartan 與 valsartan 用於原發性高血壓合併第二型糖尿病腎病變，治療 12 週；尚無結果 |

---

## 文獻證據

以下為糖尿病腎病變相關文獻（依類型優先排序，列出 10 篇）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | 臨床研究（併用治療，隨機分組 112 人） | Int Immunopharmacol | nifedipine 控釋錠加 sacubitril/valsartan 用於糖尿病腎病變合併高血壓，對照組為加 valsartan |
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | PARADIGM-HF 次分析 | Lancet Diabetes Endocrinol | 評估腦啡肽酶抑制對第二型糖尿病合併心衰竭患者腎功能的影響 |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | 臨床影像研究 | Diabetes Metab Syndr Obes | 以 BOLD-MRI 評估 sacubitril/valsartan 對糖尿病腎病變患者的腎臟保護 |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | 糖尿病腎病變治療支柱的最新進展 |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Curr Hypertens Rep | 新型降壓藥物與高血壓靶器官損傷的緩解 |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | 動物實驗（大鼠） | Diabetes Metab Syndr Obes | 透過抑制 NLRP3 發炎體路徑，改善早期糖尿病腎病變進展 |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | 動物實驗（小鼠） | Front Endocrinol | 改善糖尿病腎病變並調節腸道菌相 |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | 動物實驗（大鼠） | PeerJ | LCZ696 抑制氧化壓力、NF-κB 發炎與腎絲球硬化 |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | 動物實驗（db/db 與 KKAy 小鼠） | Am J Physiol Renal Physiol | 與 valsartan 相比，在不同小鼠模型中效果有差異 |
| [40635044](https://pubmed.ncbi.nlm.nih.gov/40635044/) | 2025 | 細胞實驗 | Eur J Med Res | LCZ696 經 Nrf2/HO-1 路徑改善高糖誘導的人類足細胞氧化壓力損傷 |

其他預測的文獻狀況：腦小血管病變僅有 1 篇文獻（PMID 37169551，主題為系統性右心室衰竭，與該疾病無關）；類風濕性關節炎僅有 1 篇個案報告（PMID 42266390，為 golimumab 相關心肌炎，不支持 sacubitril 的療效）；其餘兩個預測無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64630 | ENTRESTO TABLETS 200MG | 資料未載明 | 資料未載明 |
| HK-64631 | ENTRESTO TABLETS 50MG | 資料未載明 | 資料未載明 |
| HK-64632 | ENTRESTO TABLETS 100MG | 資料未載明 | 資料未載明 |
| HK-65170 | ENTRESTO TABLETS 100MG (SINGAPORE) | 資料未載明 | 資料未載明 |
| HK-65171 | ENTRESTO TABLETS 50MG (SINGAPORE) | 資料未載明 | 資料未載明 |

以上僅列出 5 張，共有 9 張有效單方許可證，皆由 Novartis Pharmaceuticals (HK) Limited 持有。

---

## 安全性考量

- **藥物交互作用**：共查得 6 項中度交互作用，包括 nitisinone、rosuvastatin、simvastatin、cobicistat、revefenacin、alpelisib。

其他警語與禁忌症資料請參考原廠仿單。針對預測適應症的特別考量：
- 腦小血管病變患者的腦血管脆弱，降血壓與血行動力學變化需謹慎評估。
- 糖尿病腎病變族群需監測高血鉀、低血壓與 eGFR 下降。

---

## 結論與下一步

**決策：**
- 排名第一至第二、第四、第五的預測（腦小血管病變、家族性血尿症候群、類風濕性關節炎、血紅蛋白病變）：**Hold**
- 糖尿病腎病變：**Proceed with Guardrails**（作為研究議題持續追蹤）

**理由：**
- 前述四個預測僅有模型分數，沒有相關的臨床試驗或文獻支持，機轉上也缺乏連結，且腦血管脆弱族群有潛在安全疑慮。
- 糖尿病腎病變有 1 個 Phase 4 隨機對照試驗（狀態未知，無結果）、多項動物實驗和少量臨床研究，機轉合理（RAAS 阻斷加利鈉肽增強），證據等級為 L3，尚無已完成的 Phase 3 腎臟結局試驗。

**若要推進需要：**
- 確認 NCT06501651 的試驗狀態並取得結果
- 以 eGFR、白蛋白尿等腎臟結局指標評估療效，並蒐集高血鉀、低血壓與 eGFR 下降的安全性數據
- 補充詳細的作用機轉資料與香港核准適應症、仿單警語及禁忌症
- 如考慮腦小血管病變，須先建立機轉依據與血壓相關安全性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

