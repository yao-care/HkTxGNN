---
layout: default
title: Progesterone
parent: 高證據等級 (L1-L2)
nav_order: 737
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Progesterone：預測新適應症為閉經 (Amenorrhea)（證據等級 L2）。原適應症：子宮內膜異位症、子宮內膜癌、停經後骨質疏鬆"
monitor_inn: "PROGESTERONE"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral"]
---

# Progesterone
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

# Progesterone：從子宮內膜異位症到閉經

## 一句話總結

Progesterone（黃體素）是天然的性類固醇荷爾蒙，原本用於子宮內膜異位症、子宮內膜癌、停經後骨質疏鬆等適應症。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，
目前有 **4 個臨床試驗**和 **20 篇文獻**支持這個方向，但這些試驗多為雌激素合併週期性黃體素的replacement 研究，並非單獨測試黃體素。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜異位症、子宮內膜癌、停經後骨質疏鬆（依知識圖譜適應症資料；許可證未載明核准適應症文字） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.9996% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，黃體素是女性生殖系統中控制子宮內膜週期變化的主要荷爾蒙，並參與調控下視丘—腦下垂體的促性腺激素分泌。

閉經常見於低雌激素或無排卵狀態。臨床上會用黃體素做「黃體素挑戰試驗」：給藥後若出現退縮性出血，表示內源性雌激素足夠且子宮流出道通暢；黃體素也用於誘發退縮性出血，並在雌激素存在時保護子宮內膜。因此，其荷爾蒙作用與閉經的診斷和處置在機轉上相符。

需要注意的是，相關臨床試驗（運動員下視丘性閉經、厭食症）主要研究雌激素合併週期性黃體素對骨骼、心血管及神經生物學的影響，黃體素是replacement 療法的標準組成，但並非唯一被測試的藥物。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | 完成 | 121 | 年輕運動員閉經的體組成與荷爾蒙變化；比較經皮或口服雌激素對骨密度的效果（相關性中等，無法確認黃體素為受試藥） |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | 完成 | 110 | 厭食症青少女的骨量與荷爾蒙；雌激素對骨發育的影響（相關性中等，終點為骨骼而非閉經緩解） |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | 進行中（不再招募） | 120 | 經皮雌二醇搭配週期性黃體素 vs 安慰劑，對飲食障礙者認知彈性與獎賞處理的影響（間接相關） |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | 完成 | 29 | 功能性下視丘閉經年輕女性的血管功能與發炎標記（間接相關，終點為心血管／免疫） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | 口服微粒化黃體素在內分泌的診斷與治療用途，包括調控促性腺激素與內膜週期 |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | 早發性卵巢功能不全的病因、症狀與治療選項 |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | 停經後陰道出血的臨床處置 |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Semin Reprod Med | 子宮內粘連（Asherman 症候群），表現可從閉經到月經正常 |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | 閉經的評估流程，須先排除懷孕 |
| [8865137](https://pubmed.ncbi.nlm.nih.gov/8865137/) | 1996 | Review | Maturitas | 荷爾蒙replacement 療法的臨床效益與副作用 |
| [24157186](https://pubmed.ncbi.nlm.nih.gov/24157186/) | 2013 | Review | Presse Med | 早發性卵巢衰竭以閉經為臨床線索，需檢測 FSH 確診 |
| [7457308](https://pubmed.ncbi.nlm.nih.gov/7457308/) | 1980 | Review | Am Fam Physician | 閉經的診斷步驟，包含黃體素給藥後是否出現退縮性出血 |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | 文獻回顧 | Gynecol Endocrinol | 排卵的神經內分泌控制，下視丘功能失常可導致無排卵與閉經 |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | 文獻回顧 | South Med J | 原發性卵巢功能不全常導致續發性閉經，需荷爾蒙replacement 療法 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44527 | CRINONE VAGINAL GEL 8% | 陰道凝膠 | 資料未載明 |
| HK-34022 | PROGESTOGEL GEL 1% | 凝膠 | 資料未載明 |
| HK-64210 | LUTINUS VAGINAL TABLETS 100MG | 陰道錠 | 資料未載明 |
| HK-61091 | UTROGESTAN VAGINAL CAP 200MG | 陰道膠囊 | 資料未載明 |
| HK-51916 | ENDOMETRIN VAGINAL TAB 100MG | 陰道錠 | 資料未載明 |

（共 9 張有效許可證，均為單一成分製劑，另有 CYCLOGEST SUPP 400MG、UTROGESTAN CAP 100MG、ZESBINA 200／100 CAPSULES 等；以上僅列 5 張。劑型依品名推斷。）

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單文字，僅供參考）：高血壓、肝衰竭／肝病、癲癇、卟啉症、腎臟病、膽囊疾病、高血糖／糖尿病、甲狀腺低下、骨質疏鬆、系統性紅斑狼瘡、氣喘、高三酸甘油脂血症、焦慮與情緒障礙、物質濫用／依賴等。
- **藥物交互作用**：共查得 100 筆，以下為部分中度（Moderate）交互作用：
  - 降血糖藥：Acarbose、Metformin、Pioglitazone、Glimepiride、Repaglinide、Chlorpropamide、Alogliptin、Saxagliptin
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - GLP-1 類：Albiglutide、Dulaglutide、Liraglutide、Semaglutide
  - 胰島素：Insulin aspart、Insulin degludec、Insulin detemir
  - 其他：Aprepitant、Clarithromycin

  整體而言，黃體素可能影響血糖控制，併用降血糖藥物時需留意。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 黃體素在閉經的診斷與處置上有明確的臨床地位，且有 1 個已完成的 Phase 3 試驗與 1 個 Phase 2/3 試驗處於相關族群；但這些試驗的受試藥主要是雌激素，黃體素的獨立貢獻尚無法確認。
- 本次預測列出的其他疾病（乳房纖維囊腫、良性乳腺發育不良、子宮頸子宮內膜異位症）僅有間接文獻，建議 Hold；雙側腎發育不全則無合理機轉，屬於知識圖譜關聯的可能假象。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌，並確認各製劑的核准適應症與給藥途徑是否涵蓋閉經
- 釐清黃體素單獨使用與合併雌激素的療效，設計針對黃體素的對照試驗
- 針對高血壓、肝病、糖尿病等族群擬定安全性監測計畫，並留意與降血糖藥的交互作用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

