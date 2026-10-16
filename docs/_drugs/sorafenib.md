---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 827
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sorafenib：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L5）。原適應症：肝細胞癌、腎細胞癌、甲狀腺癌"
---

# Sorafenib
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

# Sorafenib：從肝細胞癌到脂肪肉瘤

## 一句話總結

Sorafenib 是一種多標靶激酶抑制劑，原本用於肝細胞癌、腎細胞癌及甲狀腺癌的治療。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個 Phase 2 臨床試驗**和 **8 篇文獻**與此方向相關，但多屬間接證據，脂肪肉瘤的特異療效尚未被證實。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肝細胞癌、腎細胞癌、甲狀腺癌（依知識圖譜適應症資料；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2（僅有 1 個已完成的多組織型 Phase 2 試驗，為間接證據，實際強度偏弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold（列為研究問題，尚不宜推進） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠資料欄位未提供）。根據已知資訊，Sorafenib 是多標靶激酶抑制劑，作用於 RAF/MEK/ERK 訊號路徑，以及 VEGFR、PDGFR 等與腫瘤生長及血管新生相關的受體。

這些路徑也與軟組織肉瘤的生長和血管新生有關。前臨床研究（如病人來源之原位異種移植模型、去分化脂肪肉瘤異種移植模型顯示 PTEN 下調）支持路徑上的相關性。

不過，軟組織肉瘤的臨床反應高度依賴組織亞型，目前並無證據顯示 Sorafenib 對脂肪肉瘤有特異活性。高預測分數可能部分反映知識圖譜中疾病之間的鄰近關係，不應直接視為療效證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | Sorafenib 用於晚期軟組織肉瘤的單臂、多組織型研究；脂肪肉瘤僅為其中一個子群，屬間接證據。相關已發表結果（S0505）顯示在多個亞型活性有限 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 試驗（SWOG S0505） | Cancer | Sorafenib 用於晚期軟組織肉瘤的多組織型研究，作用靶點包括 RAF、VEGFR1-3、PDGFR-B、FLT3、c-kit |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 試驗 | Ann Surg Oncol | 術前保形放療併用 Sorafenib 治療肢體局部晚期軟組織肉瘤 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | 依組織亞型選擇軟組織肉瘤的藥物治療 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 軟組織肉瘤的組織型導向與非組織型導向治療；trabectedin 對脂肪肉瘤活性較突出 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review（前臨床 PDOX 模型） | Front Oncol | 以 PDOX 模型找出 palbociclib 的有效組合療法 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 前臨床研究 | Mol Cancer Ther | Sorafenib 抑制惡性周邊神經鞘瘤細胞生長及 MAPK 訊號（含去分化脂肪肉瘤細胞株，但主要為 MPNST） |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 前臨床異種移植研究 | Am J Pathol | 去分化脂肪肉瘤模型顯示 PTEN 下調，並對 PI3K 路徑抑制有反應 |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | 個案報告 | Anti-Cancer Drugs | Trabectedin 用於滑膜肉瘤肺轉移（非 Sorafenib，亦非脂肪肉瘤） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55409 | NEXAVAR TAB 200MG（Bayer） | 錠劑 | 資料未載明 |
| HK-67562 | SORAFENIB STADA TABLETS 200MG | 錠劑 | 資料未載明 |
| HK-66345 | SORAFENAT TABLETS 200MG | 錠劑 | 資料未載明 |
| HK-68075 | RAFALVO TABLETS 200MG | 錠劑 | 資料未載明 |
| HK-68600 | SORAFENIB TABLETS USP 200MG | 錠劑 | 資料未載明 |

另有 HK-68700（SORAFENIB SANDOZ TABLETS 200MG），合計 6 張有效許可證，皆為單方製劑，無已註銷者。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶激酶抑制劑），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 請參考原廠仿單；知識圖譜列有血小板低下、嗜中性白血球低下等相關禁忌疾病訊號 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測 CBC、肝功能、血壓、電解質（含血磷） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜標示之相關疾病（非仿單內容）**：高血壓、肝衰竭、血小板低下、嗜中性白血球低下、粒線球缺乏症、凝血疾病、急性冠心症／冠狀動脈疾病／心肌梗塞、心肌缺血、貧血、低血磷、胰臟炎、焦慮及神經症相關疾患等。
- **藥物交互作用**：共查得 100 筆，以下為部分示例。
  - 重度：Dolasetron
  - 中度：Famotidine、Loperamide、Dexamethasone、Clarithromycin、Levofloxacin、Palonosetron、Naltrexone 等
  - 輕度：Dapagliflozin、Metronidazole、Naloxegol

仿單的警語與禁忌症資料尚未取得，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 脂肪肉瘤僅有 1 個多組織型 Phase 2 試驗，且為間接證據，相關已發表結果顯示在多個軟組織肉瘤亞型活性有限，脂肪肉瘤特異療效並未被證明。
- 其餘預測（卵巢黏液脂肪肉瘤、TFE3 相關腎細胞癌等）僅有模型分數支持，且多半源自既有腎細胞癌適應症的疾病鄰近關係，並非新的再利用訊號。

**若要推進需要：**
- 取得 SWOG S0505 與 NCT00217620 中脂肪肉瘤子群的分組療效數據
- 補充詳細作用機轉資料及脂肪肉瘤特異性的機轉證據
- 取得香港仿單的警語、禁忌症與核准適應症文字，完成安全性篩查
- 若仍有興趣，可考慮設計針對脂肪肉瘤亞型（如去分化型）的小型探索性研究，並與現有標準治療（如 trabectedin、eribulin）比較
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

