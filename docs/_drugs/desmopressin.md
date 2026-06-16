---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin：從止血/抗利尿 到 先天性凝血酶原缺乏症

## 一句話總結

Desmopressin（DDAVP，去氨加壓素）是血管加壓素的合成類似物，國際上廣泛用於中樞性尿崩症、夜間遺尿症及輕型血友病A／第一型 von Willebrand 病的止血輔助治療。
TxGNN 模型預測其最高分潛在新適應症為**先天性凝血酶原缺乏症（Congenital Prothrombin Deficiency）**，然而本次多適應症評估涵蓋十項罕見出血與血小板疾病，目前有 **2 個臨床試驗**（與排名 #1、#8 相關）及 **50+ 篇文獻**支持各方向研究，其中**Glanzmann 血小板無力症（排名 #3）**與**血小板原發性釋放障礙（排名 #4）**具備最強的臨床可行性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 中樞性尿崩症、夜間遺尿症、輕型血友病A、第一型 vWD（國際適應症；香港未上市） |
| 預測新適應症（最高分） | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L4（排名 #1 適應症）|
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 總預測適應症數 | 10 項 |
| 建議決策 | Hold（排名 #1）；最優先候選見下方 |

---

## 為什麼這個預測合理？

Desmopressin 的核心藥理機轉是與內皮細胞上的 V2 受體結合，觸發 Weibel-Palade body 釋放儲存的 von Willebrand 因子（vWF）及第 VIII 凝血因子（Factor VIII）進入循環，同時增加血小板膜上 GP1b 受體的表現量，進而縮短出血時間。此一機轉使其在 vWF 相關出血疾病中具有明確的止血基礎。

先天性凝血酶原缺乏症（Factor II 缺乏症）為罕見常染色體隱性遺傳凝血障礙，主要病理為凝血酶原（Prothrombin）量化或功能性不足，導致凝血酶（Thrombin）生成障礙。**Desmopressin 的 vWF/Factor VIII 釋放機轉對 Factor II 缺乏並無直接補充效果**，兩者的機轉關聯性薄弱，需釐清是否存在間接性止血輔助作用。

現有相關文獻（1989–1993 年）主要涉及 Factor V/Factor VIII 聯合缺乏症個案，與純粹的凝血酶原缺乏適應症僅有間接關聯。TxGNN 的高分預測可能源於知識圖譜中廣泛出血疾病節點的網絡鄰近效應，而非直接藥理機轉連結。

---

## 臨床試驗證據（先天性凝血酶原缺乏症）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | 招募中 | 20 | Emicizumab（非 Desmopressin）用於輕型血友病A的凝血特性及止血療效評估；研究藥物與適應症均非本候選，相關性極低，僅顯示出血疾病領域有研究活動 |

---

## 文獻證據（先天性凝血酶原缺乏症）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | 常見遺傳性出血疾病的合理治療選項評估；指出 DDAVP 可用於輕型血友病A及多數 vWD 患者，視安全性、療效與成本效益而定 |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 後天性血友病A（自體抗體對抗 Factor VIII）的診斷、病因及治療概述；與凝血酶原缺乏無直接關聯 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | DDAVP 用於先天性 Factor V+VIII 聯合缺乏症個案；給藥後出血時間縮短，提示 DDAVP 對部分複合凝血因子缺乏有輔助效果 |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | 先天性 Factor V+VIII 聯合缺乏症孕婦剖腹產的 Factor VIII 替代療法管理；DDAVP 作為圍術期輔助用藥 |

---

## 十項預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策建議 | 特別提示 |
|------|--------|-----------|---------|---------|---------|
| 1 | 先天性凝血酶原缺乏症 | 99.70% | L4 | Hold | 機轉關聯性薄弱 |
| 2 | 遺傳性血栓傾向 | 99.44% | L4 | Hold | ⚠️ 潛在禁忌：可能加重血栓風險 |
| 3 | **Glanzmann 血小板無力症** | **99.30%** | **L3** | **Proceed with Guardrails** | 現行指引已列為一線輔助治療 |
| 4 | **血小板原發性釋放障礙** | **99.26%** | **L3** | **Proceed with Guardrails** | 有前瞻性研究直接支持 |
| 5 | 假性 von Willebrand 病 | 99.16% | L4 | Hold | ⚠️ 安全性疑慮：可能加劇消耗性血小板減少 |
| 6 | Scott 症候群 | 99.16% | L5 | Hold | 機轉無直接關聯 |
| 7 | Flood 因子缺乏症 | 99.15% | L5 | Hold | 疾病命名不明確，疑為資料品質問題 |
| 8 | 血小板減少性紫癜 | 98.95% | L4 | Research Question | 需嚴格區分 ITP vs TTP 亞型再評估 |
| 9 | 膠原蛋白受體缺陷出血疾病 | 98.95% | L4 | Research Question | 間接機轉，需更多針對性研究 |
| 10 | 遺傳性血小板增多症合併橫向肢體缺陷 | 98.95% | L5 | Hold | 極罕見，無任何相關文獻 |

---

## 最優先候選：Glanzmann 血小板無力症（排名 #3）

**機轉連結**：Glanzmann 血小板無力症（GT）為 αIIbβ3 整合素（GP IIb/IIIa）缺陷導致血小板聚集功能喪失。Desmopressin 雖無法修復受體缺陷，但可透過釋放超大型 vWF 多聚體（ULvWF）提供替代性血小板黏附途徑（透過 GP1b 受體），作為輕中度出血的輔助止血藥物。**現行國際指引（GTH S2K 指引、WFH 指引）已明確將 Desmopressin 列為 GT 的一線輔助治療選項之一。**

**代表性文獻（共 20 篇，列出前 10 篇）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19967146](https://pubmed.ncbi.nlm.nih.gov/19967146/) | 2009 | Expert Consensus / Guideline | Thrombosis and Haemostasis | GT 管理建議共識；納入 DDAVP 作為輕中度出血的輔助止血選項 |
| [22726101](https://pubmed.ncbi.nlm.nih.gov/22726101/) | 2012 | Review / Guideline | Haemophilia | 遺傳性血小板疾病治療指引（WFH）；GT 嚴重出血用血小板輸注，輕中度可考慮 DDAVP |
| [25370176](https://pubmed.ncbi.nlm.nih.gov/25370176/) | 2014 | S2K Clinical Guideline | Hamostaseologie | 德國止血學會（GTH）跨科際遺傳性血小板功能疾病治療指引 |
| [41301446](https://pubmed.ncbi.nlm.nih.gov/41301446/) | 2025 | Review | Biomolecules | 遺傳性血小板功能障礙分子病理機制最新綜述；涵蓋 GT 的 ITGA2B/ITGB3 突變致病機轉 |
| [16722529](https://pubmed.ncbi.nlm.nih.gov/16722529/) | 2006 | Review | Orphanet J Rare Dis | GT 全面綜述；臨床異質性、分子基礎及治療選項（含 DDAVP） |
| [30097224](https://pubmed.ncbi.nlm.nih.gov/30097224/) | 2018 | Systematic Review | Transfusion Medicine Reviews | 孕產婦遺傳性出血疾病管理系統性回顧；止血選項包含 DDAVP |
| [32610148](https://pubmed.ncbi.nlm.nih.gov/32610148/) | 2020 | Observational Study | J Pediatr Adolesc Gynecol | 遺傳性血小板功能障礙青少年月經過多的門診治療模式與療效評估 |
| [16444446](https://pubmed.ncbi.nlm.nih.gov/16444446/) | 2006 | Case Report | Clin Appl Thromb/Hemost | GT 患者牙科拔牙：rFVIIa + DDAVP 合用成功止血；DDAVP 單獨效果有限 |
| [10509036](https://pubmed.ncbi.nlm.nih.gov/10509036/) | 1999 | Clinical Study | Haematologica | DDAVP 對血小板功能體內外效應研究；探討 DDAVP 在血小板功能障礙中的作用機轉 |
| [1785670](https://pubmed.ncbi.nlm.nih.gov/1785670/) | 1991 | Clinical Study | Am J Pediatr Hematol/Oncol | DDAVP + etamsylate 協同縮短出血時間；GT（n=1）及其他血小板功能障礙患者 |

---

## 次優先候選：血小板原發性釋放障礙（排名 #4）

**機轉連結**：血小板原發性釋放障礙（如 δ-storage pool 缺乏症、阿斯匹靈樣缺陷）導致 ADP 及血清素釋放不足，影響血小板活化放大訊號。Desmopressin 透過釋放 ULvWF 並增加血小板膜 GP1b 受體數量，提供替代性活化途徑。**已有前瞻性小兒研究（PMID 21509710）直接評估 DDAVP 對遺傳性血小板功能病的療效，並有 2023 年系統性回顧（PMID 36656570）提供廣泛文獻支持。**

**代表性文獻：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Systematic Review | Eur J Haematology | DDAVP 作為止血與節血藥物的系統性回顧；支持用於輕型血友病A、vWD 及血小板功能障礙（含釋放缺陷）|
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Prospective Study | Klin Padiatr | DDAVP 對阿斯匹靈樣缺陷（遺傳性血小板病）兒童初級止血效果的直接前瞻性評估 |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Mechanistic Study | Haemophilia | DDAVP 後 vWF 結合至血小板微粒顯著增加；提示 DDAVP 止血效果存在 FVIII/VWF 提升以外的額外機轉 |
| [1613990](https://pubmed.ncbi.nlm.nih.gov/1613990/) | 1992 | Clinical Study | Nihon Rinsho | DDAVP 對各類血小板功能障礙（共 17 例）止血控制效果；阿斯匹靈樣缺陷患者出血時間縮短 |

---

## ⚠️ 安全性警示：不建議推進之適應症

以下兩項 TxGNN 高分預測適應症具有潛在嚴重安全疑慮：

**遺傳性血栓傾向（排名 #2）**：Desmopressin 大量釋放 ULvWF 多聚體，可能增加血栓形成風險。遺傳性血栓傾向患者（如 Factor V Leiden、Protein C/S 缺乏、Prothrombin G20210A 突變）本身已有高凝狀態，使用 Desmopressin 可能加劇血栓風險。PMID 16460464 明確指出此連結為「出乎意料的危險關聯（unexpected link）」，建議 **Hold** 並列為禁忌候選。

**假性 von Willebrand 病（排名 #5）**：此病（亦稱血小板型 vWD）為 GP1bα 功能增益突變，血小板對 vWF 親和力異常過高。Desmopressin 釋放大量 ULvWF 可能觸發過度血小板聚集，反而引發**消耗性血小板減少症**。部分文獻明確提示此為 Desmopressin 的潛在禁忌症，建議 **Hold**。

---

## 香港上市資訊

Desmopressin 目前在香港**未取得上市許可**（許可證數量：0 張）。如需臨床使用，須透過香港衛生署特殊進口申請（Unregistered Drug Import）途徑取得。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 根據現有文獻，Desmopressin 的主要已知風險包括低血鈉症（尤其在兒童及液體攝取過多時）、面部潮紅、頭痛，以及罕見的動脈血栓事件。在特定疾病（遺傳性血栓傾向、假性 vWD、TTP）中存在禁忌或安全疑慮（詳見上方警示章節）。

---

## 結論與下一步

### 最優先推進候選

**決策：Proceed with Guardrails（Glanzmann 血小板無力症 & 血小板原發性釋放障礙）**

**理由：**
兩項適應症均已有觀察性研究、系統性回顧及國際臨床指引（L3 等級）支持 Desmopressin 作為輔助止血藥物；機轉上透過 ULvWF 釋放提供替代性黏附途徑，具合理的科學基礎，且現行指引已將其納入一線輔助選項。

### 排名 #1 適應症

**決策：Hold（先天性凝血酶原缺乏症）**

**理由：**
TxGNN 高分預測可能源於知識圖譜網絡效應，而非直接藥理機轉連結。Desmopressin 的 vWF/Factor VIII 釋放機轉對 Factor II（凝血酶原）缺乏無直接補充效果，現有文獻亦以 Factor V/VIII 聯合缺乏症間接個案為主，缺乏針對凝血酶原缺乏的直接臨床證據。

### 若要推進最優先候選需要：

- 向香港衛生署申請 Desmopressin 特殊進口許可，確認供應鏈可行性
- 取得原廠仿單，完整評估警語、禁忌症及藥物交互作用
- 制定患者篩選標準：排除遺傳性血栓傾向及假性 vWD 患者
- 訂定臨床使用方案：
  - 適應輕中度出血情境（嚴重出血仍需血小板輸注或 rFVIIa）
  - 靜脈給藥（0.3 μg/kg）或鼻噴劑的選擇依據
  - 低血鈉症監測計畫（給藥後 8 小時內監測血清鈉值，尤其兒童）
  - 快速脫敏（tachyphylaxis）評估與間隔管理方案（建議給藥間隔 ≥24 小時）
- 考慮向 WHO Orphan Drug 或在地罕見疾病藥物計畫申請，以利長期供應保障
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

