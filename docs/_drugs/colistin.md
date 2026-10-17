---
layout: default
title: Colistin
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Colistin：預測新適應症為感染後血管炎 (Postinfectious Vasculitis)（證據等級 L5）。原適應症：大腸桿菌感染、外耳炎、外耳疾病"
monitor_inn: "COLISTIN"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
---

# Colistin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Colistin：從大腸桿菌感染與外耳炎到慢性鼻竇炎（鼻竇炎）

## 一句話總結

Colistin（黏菌素）是多黏菌素類抗生素，原本用於治療大腸桿菌感染與外耳炎等革蘭氏陰性菌相關感染。
TxGNN 模型的前幾名預測（如感染後血管炎）缺乏任何研究支持，證據較多的預測是**鼻竇炎 (Sinusitis)**，目前有 **0 個臨床試驗**和 **11 篇相關文獻**，但多為病例報告、綜述或前臨床研究，屬於研究假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 大腸桿菌感染、外耳炎、外耳疾病（香港許可證未登載適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 感染後血管炎 (Postinfectious Vasculitis)（排名第 1）；證據較多者為鼻竇炎 (Sinusitis)（排名第 8） |
| TxGNN 預測分數 | 感染後血管炎 99.91%；鼻竇炎 99.25% |
| 證據等級 | 感染後血管炎 L5；鼻竇炎 L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（鼻竇炎方向可列為 Research Question） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，colistin 是多黏菌素類抗生素，會破壞革蘭氏陰性菌的外膜，對綠膿桿菌等多重抗藥性革蘭氏陰性菌有殺菌作用。

**排名第 1 的預測（感染後血管炎）**機轉上缺乏合理連結。此疾病屬感染後的免疫媒介反應，colistin 最多只能透過清除誘發病原體產生間接作用。此外 colistin 具腎毒性，對血管炎患者是顧慮。排名 2–6 的預測（感染後疾病、感染後症候群、恰加斯心肌病變、感染相關溶血性尿毒症候群、感染性尿道狹窄）同樣缺乏機轉依據，且部分情況（如 STEC 相關 HUS）通常避免使用抗生素。

**證據較多的方向是鼻竇炎。**囊狀纖維化及免疫低下患者的鼻竇炎常由綠膿桿菌等革蘭氏陰性菌引起，colistin 對這些菌有活性，因此機轉上有合理性。慢性鼻竇炎與慢性篩竇炎的支持程度較低，主要依據類推。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為排名第 8 的鼻竇炎預測相關文獻（優先列出與 colistin 較直接相關者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | 囊狀纖維化合併慢性鼻竇炎的治療選項綜述，此類鼻竇炎常對標準治療反應不佳 |
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Case report | Int J Hematol | 急性骨髓性白血病患者因多重抗藥性綠膿桿菌引起鼻竇炎、眼眶蜂窩性組織炎與肺炎，靜脈注射 colistin 治療成功 |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | 藥物動力學研究 | J Antimicrob Chemother | 囊狀纖維化患者經鼻給予 tobramycin 與 colistin（CMS）後有系統性吸收，與安全性評估相關 |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | 體外/前臨床 | Int J Antimicrob Agents | colistin 對綠膿桿菌的殺菌作用不依賴氫氧自由基形成 |
| [33155505](https://pubmed.ncbi.nlm.nih.gov/33155505/) | 2021 | 前臨床/給藥方法 | Acta Otolaryngol | 自體纖維蛋白膠合併抗生素，可用於鼻竇手術後局部抗生素治療 |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | 體外/前臨床 | Pharmaceutics | Ceragenins 合併 ivacaftor 可抑制引起鼻竇炎細菌的生物膜形成（非 colistin 研究） |

其餘文獻（如原發性纖毛不動症鼻竇手術、嗜中性白血球低下發燒研究、耳鼻喉科綠膿桿菌抗藥性回溯研究等）與 colistin 療效僅為間接相關，故未列出。

排名 7 的副傷寒另有 1 篇 1964 年的臨床觀察報告（[14126225](https://pubmed.ncbi.nlm.nih.gov/14126225/)，Iryo），未顯示 colistin 療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63662 | COLISTIN POWDER FOR SOLUTION FOR INJECTION 150MG | 未登載 | 未登載 |
| HK-42135 | MULTIBIO SUSPENSION INJ (VET) | 未登載 | 未登載 |

HK-42135 為獸醫用產品，不適用於人類。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單內容）：腎臟疾病、輸尿管積膿、單純皰疹感染、困難梭狀桿菌結腸炎、新生兒壞死性腸炎、重症肌無力（含成人型）、神經肌肉接合部疾病、膝狀神經節帶狀皰疹、出血性大皰性鼓膜炎。
- **腎毒性**：colistin 具腎毒性，在感染後血管炎與溶血性尿毒症候群等腎臟受損情境尤須注意。
- **鼻腔給藥**：已有研究顯示經鼻給藥仍有系統性吸收，需評估安全性。

其他警語與藥物交互作用資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（鼻竇炎方向可列為 Research Question）

**理由：**
- 預測分數最高的前 6 項皆僅有模型預測，無臨床試驗或文獻，且機轉連結薄弱或不成立，另有腎毒性顧慮。
- 鼻竇炎（尤其是囊狀纖維化或免疫低下患者的綠膿桿菌感染）有合理機轉及少量病例報告，但沒有臨床試驗，證據僅為 L4。

**若要推進需要：**
- 取得詳細的作用機轉（MOA）資料。
- 取得香港仿單的警語與禁忌，完成安全性篩選。
- 針對鼻竇炎設計局部或吸入給藥的安全性與療效研究，並評估系統性吸收與腎毒性。
- 確認給藥途徑與現有劑型（注射劑）的相容性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

