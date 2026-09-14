---
layout: default
title: Sacubitril
parent: 中證據等級 (L3-L4)
nav_order: 670
evidence_level: L3
indication_count: 5
---

# Sacubitril
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Sacubitril：從心衰竭（ARNI 複方成分）到糖尿病腎病變

## 一句話總結

Sacubitril 是 ARNI（Entresto/LCZ696）複方中的 neprilysin 抑制劑前驅藥，目前臨床上與 valsartan 併用治療心衰竭（HFrEF），此單體本身尚未於香港上市。TxGNN 模型對此藥物共預測 5 個新適應症，其中僅**糖尿病腎病變**有實質證據支持，目前有 **2 個臨床試驗**和 **17 篇文獻**（多為動物實驗與世代研究），其餘 4 個候選（含分數最高者）皆無臨床試驗或文獻佐證，機轉關聯性也薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心衰竭（HFrEF）— 作為 ARNI 複方（sacubitril/valsartan）成分，非 sacubitril 單體核准適應症 |
| 預測新適應症 | 糖尿病腎病變 (Diabetic Nephropathy) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（列為研究問題） |

---

## 為什麼這個預測合理？

目前缺乏 Sacubitril 單體的完整作用機轉登錄資料（Data Gap）。根據證據內文可知，Sacubitril 是 neprilysin 抑制劑前驅藥，經代謝生成活性代謝物 sacubitrilat 後抑制 neprilysin，減少利鈉胜肽（ANP/BNP）的降解，藉此提升利鈉、擴血管與抗纖維化作用；臨床上以 sacubitril/valsartan 複方形式（Entresto/LCZ696）用於心衰竭治療。

心衰竭與糖尿病腎病變在病理生理上高度重疊：兩者皆涉及 RAAS（腎素-血管收縮素-醛固酮系統）過度活化、腎絲球內高壓與慢性發炎纖維化。Sacubitril 與 valsartan 併用形成雙重 RAAS-neprilysin 阻斷，機轉上可能降低腎絲球內高壓、減少白蛋白尿，對糖尿病腎病變具理論保護作用，這也是多篇動物實驗（NLRP3 發炎小體抑制、氧化壓力改善、腎臟血流增加）的共同結論。

**需特別注意的限制**：本評估的藥物實體是 sacubitril 單體（DB09292），但幾乎所有支持證據都來自 sacubitril/valsartan **複方**（無法排除 valsartan 本身對腎臟的獨立保護作用），且此複方在香港尚未上市。因此證據雖然方向一致，但無法直接歸因於 sacubitril 單一成分的效果。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | 尚未招募 | 297 | 多中心 RCT，比較 sacubitril/valsartan 與 valsartan 治療輕中度高血壓合併第二型糖尿病腎病變，尚無療效資料 |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | 已完成 | 268 | 印度真實世界回溯性研究，主族群為 HFrEF 患者，非以糖尿病腎病變為主要終點，僅間接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | RCT 次分析 | Lancet Diabetes Endocrinol | PARADIGM-HF 試驗次分析：neprilysin 抑制對第二型糖尿病合併慢性心衰竭患者的腎功能有正面影響 |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Cohort | Diabetes Metab Syndr Obes | 以 BOLD-MRI 評估 sacubitril/valsartan 對第二型糖尿病患者的腎臟保護效果 |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Cohort | Int Immunopharmacol | 112 名糖尿病腎病變合併高血壓患者，sacubitril/valsartan 併用 nifedipine 改善腎功能 |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | 糖尿病腎病變治療進展回顧，涵蓋 RAAS 阻斷及新興療法 |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | 動物實驗 | Diabetes Metab Syndr Obes | Sacubitril/valsartan 透過抑制 NLRP3 發炎小體路徑改善早期糖尿病腎病變（大鼠） |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | 動物實驗 | Front Endocrinol | Sacubitril/valsartan 改善糖尿病腎病並調節腸道菌相（小鼠） |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | 動物實驗 | PeerJ | LCZ696 透過抑制氧化壓力、NF-κB 發炎與腎絲球硬化減緩糖尿病腎病變（大鼠） |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | 動物實驗 | Am J Physiol Renal Physiol | Sacubitril/valsartan 在 db/db 與 KKAy 小鼠模型中對糖尿病腎病有不同調節效果 |
| [30909895](https://pubmed.ncbi.nlm.nih.gov/30909895/) | 2019 | 動物實驗 | Cardiovasc Diabetol | Sacubitril 與 valsartan 併用比 valsartan 單用更能減輕 Zucker 肥胖大鼠的腎絲球與腎小管損傷 |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Rev Med Suisse | Sacubitril/valsartan 在第二型糖尿病中的潛在角色綜述 |

---

## 香港上市資訊

Sacubitril 目前**尚未於香港上市**（未取得任何許可證登記）。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估未取得 TFDA/HK 仿單警語、禁忌症及藥物交互作用資料，屬 Blocking 等級資料缺口，需另行下載複方 Entresto 仿單補齊）

---

## 其他 TxGNN 候選適應症（已排除）

本次評估另有 4 個 TxGNN 高分預測，因無臨床試驗、無文獻佐證，且機轉關聯性薄弱，暫不建議推進：

| 排名 | 預測適應症 | TxGNN 分數 | 排除原因 |
|------|-----------|-----------|---------|
| 1 | Brain small vessel disease 1（COL4A1 相關遺傳病） | 99.58% | 致病機轉為第四型膠原蛋白結構異常，與 neprilysin/利鈉胜肽路徑無已知關聯，模型分數屬統計關聯而非生物學合理性 |
| 2 | HANAC 症候群（COL4A1 相關） | 99.57% | 同上，無任何臨床試驗或文獻支持 |
| 4 | 類風濕性關節炎 | 99.35% | 無臨床試驗或文獻；neprilysin 與 RA 主要致病路徑（TNF-α、IL-6）無直接連結 |
| 5 | 血紅蛋白病 | 99.18% | 無臨床試驗或文獻；為血紅素基因結構異常疾病，與 neprilysin 抑制機轉無已知關聯 |

---

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 糖尿病腎病變候選有 L3 等級證據（人類世代研究＋RCT 次分析＋多篇動物機轉研究），方向一致且具生物學合理性，但關鍵限制是幾乎所有證據來自 sacubitril/valsartan **複方**而非 sacubitril 單體，且此複方在香港尚未上市，唯一直接鎖定此適應症的 Phase 4 RCT（NCT06501651）尚未開始招募。
- 其餘 4 個 TxGNN 高分候選經證據檢視後均無臨床或文獻支持，已排除。

**若要推進需要：**
- 補齊 TFDA/HK 仿單警語、禁忌症與藥物交互作用資料（Blocking 缺口 DG001）
- 補齊 Sacubitril 完整作用機轉資料，釐清 sacubitril 單體 vs. valsartan 併用對腎臟保護效果的貢獻比例（High 缺口 DG002）
- 追蹤 NCT06501651 招募與期中結果，作為是否進入下一階段的關鍵觸發點
- 確認香港是否已有 sacubitril/valsartan 複方（Entresto）上市及其核准適應症範圍
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

