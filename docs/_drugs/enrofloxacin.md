---
layout: default
title: Enrofloxacin
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Enrofloxacin
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

# Enrofloxacin：從（原適應症未載明）到心臟疾病（Heart Disease）

## 一句話總結

Enrofloxacin 是一種氟喹�olone（fluoroquinolone）類抗菌藥，在香港僅以獸醫用途的產品上市。
TxGNN 模型預測它可能對**心臟疾病 (Heart Disease)** 有效，但目前**沒有任何臨床試驗**，且 20 篇文獻幾乎全為獸醫或動物研究，**無法支持**這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未載明（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 心臟疾病 (Heart Disease) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4（僅有動物與機轉層級資料，無人體研究） |
| 香港上市 | ✓ 已上市（獸醫用） |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Enrofloxacin 是氟喹諾酮類抗菌藥，
一般認為其作用是抑制細菌 DNA gyrase 與拓撲異構酶 IV，用於治療細菌感染。

就機轉來看，抑制細菌酵素與心臟疾病之間**沒有可信的連結**。
TxGNN 的高分（99.94%）來自知識圖譜的關聯推論，並非來自生物學或臨床證據。
同一批預測中，多個彼此無關的先天性或結構性疾病（如 Pierre Robin 症候群、染色體缺失）也都拿到近乎相同的高分，
顯示分數可能反映圖譜鄰近節點的相似性，而非真實療效。

另一方面，氟喹諾酮類在人體已有心血管安全性警訊（QT 延長、主動脈瘤／主動脈剝離），
這些與擬新增的心臟適應症方向相反。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

系統共檢索到 20 篇文獻，皆為獸醫、動物或環境研究。以下列出與心臟相關、最相關的項目：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31226987](https://pubmed.ncbi.nlm.nih.gov/31226987/) | 2019 | Review | BMC Veterinary Research | 氟喹諾酮（含 enrofloxacin）對雞胚的生殖毒性，屬毒性研究 |
| [34157764](https://pubmed.ncbi.nlm.nih.gov/34157764/) | 2021 | Case report | Tierarztliche Praxis K | 一隻貓疑似心肌炎併發充血性心衰竭，藥物非治療重點 |
| [41190687](https://pubmed.ncbi.nlm.nih.gov/41190687/) | 2025 | Case report | J Am Anim Hosp Assoc | 一隻犬感染 Brucella canis 併心肌炎，enrofloxacin 為抗菌治療之一，未顯示心臟益處 |
| [33276911](https://pubmed.ncbi.nlm.nih.gov/33276911/) | 2020 | Case report | J Equine Vet Sci | 母馬使用 ceftiofur 後的藥物不良反應，非 enrofloxacin |
| [23562103](https://pubmed.ncbi.nlm.nih.gov/23562103/) | 2013 | Animal PK study | JAALAS | 非洲爪蟾組織分布，含心臟組織藥物濃度測定，非療效研究 |
| [17269886](https://pubmed.ncbi.nlm.nih.gov/17269886/) | 2007 | Animal toxicity study | Am J Vet Res | 貓高劑量口服 enrofloxacin 的眼部與全身毒性 |

其餘文獻為魚類、家禽、牲畜的感染或藥動學研究，與心臟疾病無關，屬關鍵字比對造成的雜訊。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60346 | BAYTRIL FLAVOUR TAB 50 MG (VET) | 未載明 | 未載明 |
| HK-60347 | BAYTRIL FLAVOUR TAB 15MG (VET) | 未載明 | 未載明 |

兩張許可證皆為獸醫用產品，持有者為 UNIPET HOUSE COMPANY LIMITED。目前香港沒有人用 enrofloxacin 的許可證資料。

## 安全性考量

- **藥物交互作用**：資料庫查無記錄。
- **類別風險（氟喹諾酮類）**：人體資料顯示有 QT 延長、主動脈瘤／主動脈剝離的心血管風險；在孕婦與兒童族群因軟骨與肌肉骨骼毒性疑慮，一般避免使用。
- Enrofloxacin 是獸醫產品，人體安全性資料有限。

其餘警語與禁忌症資料缺漏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻皆為獸醫或關鍵字雜訊，也沒有可信的機轉連結；氟喹諾酮的心血管安全警訊反而不利此適應症。
- 排名前 10 的其他預測（Laubry-Pezzi 症候群、Pierre Robin 症候群、心瓣膜疾病等）同樣只有模型分數，證據等級為 L5，或僅有間接證據（僧帽瓣疾病為 L4，僅一篇犬心內膜炎病例報告），皆不建議推進。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（目前為阻斷性缺口，無法進入安全性篩選）
- 補齊作用機轉資料（如 DrugBank）
- 取得任何人體層級的心臟適應症證據，並釐清其與 QT／主動脈風險的取捨
- 確認人用氟喹諾酮（如 ciprofloxacin）是否更適合作為研究對象，因 enrofloxacin 僅有獸醫用途

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

