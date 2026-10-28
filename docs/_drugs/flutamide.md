---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 8
monitor_inn: "FLUTAMIDE"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-28
description: "Flutamide：預測新適應症為攝護腺纖維瘤 (fibroma of prostate)（證據等級 L5）。原適應症：攝護腺癌"
---

# Flutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Flutamide：從攝護腺癌到攝護腺纖維瘤
{: .text-alpha }

## 一句話總結

Flutamide 是一種抗雄性素藥物，原本用於攝護腺癌治療（知識圖譜記錄的原適應症）。
TxGNN 模型預測排名第一的新適應症為**攝護腺纖維瘤 (fibroma of prostate)**，但該項目沒有任何臨床試驗或文獻支持。
本報告同時說明證據相對較多的第三名預測：**良性生殖系統腫瘤 (benign reproductive system neoplasm)**，目前有 **14 篇文獻**，但無臨床試驗，且沒有任何研究直接針對該疾病本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 攝護腺癌（來自知識圖譜記錄；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 攝護腺纖維瘤 (fibroma of prostate)（排名第一） |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

> 備註：排名第三的「良性生殖系統腫瘤」（分數 0.9998）文獻較多，但現有文獻多為攝護腺癌或良性攝護腺增生（BPH）等相關疾病的研究，並非直接針對該疾病，依規則證據等級同樣為 L5。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Flutamide 屬於雄性素受體拮抗劑，攝護腺組織依賴雄性素，因此在機轉上對雄性素依賴的攝護腺良性腫瘤（如纖維瘤、平滑肌瘤）有理論上的合理性。

不過，這些疾病極為罕見，既無臨床試驗也無文獻支持。高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，屬於模型預測，並非臨床證據。

其他預測中，Brenner 瘤（卵巢腫瘤）、HIV 感染、貓免疫缺陷症候群及猿猴免疫缺陷病毒感染，與雄性素受體阻斷缺乏已知機轉關聯，這些分數來自 TxGNN 模型（深度學習），較可能反映模型學到的相關疾病之間的相似性，並非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為「良性生殖系統腫瘤」預測所列文獻（排名第三，列出最相關者）。這些研究多探討攝護腺癌或良性攝護腺組織，並非直接研究該預測疾病。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1722793](https://pubmed.ncbi.nlm.nih.gov/1722793/) | 1991 | 世代研究 | Journal of Andrology | 良性攝護腺增生（BPH）男性使用 flutamide（750 mg/日，6 個月）的雙盲隨機試驗，評估攝護腺體積、PSA 與睪固酮反應 |
| [1989458](https://pubmed.ncbi.nlm.nih.gov/1989458/) | 1991 | 世代研究 | Am J Surg Pathol | LHRH 促效劑合併 flutamide 治療後，良性攝護腺腺體出現明顯萎縮、基底細胞增生 |
| [11829828](https://pubmed.ncbi.nlm.nih.gov/11829828/) | 1999 | 世代研究 | Zhonghua Wai Ke Za Zhi | 合併內分泌療法對正常攝護腺、BPH、攝護腺癌與睪丸的病理變化 |
| [10209490](https://pubmed.ncbi.nlm.nih.gov/10209490/) | 1998 | 未分類 | J Pathol | 長期雄性素阻斷下，良性攝護腺上皮細胞的增殖活性 |
| [26926093](https://pubmed.ncbi.nlm.nih.gov/26926093/) | 2016 | 回顧 | Pharmacol Res | 攝護腺癌中雄性素生物轉化與 UGT 酵素調控網絡 |
| [17128417](https://pubmed.ncbi.nlm.nih.gov/17128417/) | 2007 | 回顧 | Histol Histopathol | 各種治療對良性攝護腺及腺癌的組織病理影響 |
| [12855748](https://pubmed.ncbi.nlm.nih.gov/12855748/) | 2003 | 回顧 | Mol Endocrinol | 類固醇荷爾蒙受體訊號在性腺腫瘤形成中的性別差異角色 |
| [8146068](https://pubmed.ncbi.nlm.nih.gov/8146068/) | 1994 | 前臨床 | The Prostate | 大鼠攝護腺腫瘤早期暴露 flutamide 可延遲腫瘤出現並減緩生長 |
| [21128595](https://pubmed.ncbi.nlm.nih.gov/21128595/) | 2011 | 前臨床 | J Med Chem | 芳基哌嗪類化合物降低大鼠攝護腺重量，flutamide 作為對照（降低 24%） |

整體而言，證據年代久遠、規模小，且多為機轉或觀察性研究。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55925 | APO-FLUTAMIDE TAB 250MG | 未提供 | 未提供 |
| HK-52992 | FLUTA-CELL 250 TAB 250MG | 未提供 | 未提供 |
| HK-44921 | FLUTAMIDE TAB 250MG | 未提供 | 未提供 |
| HK-40974 | FLUTAN TAB 250MG | 未提供 | 未提供 |

---

## 細胞毒性

Flutamide 為攝護腺癌用的抗雄性素藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 荷爾蒙/標靶類（雄性素受體拮抗劑），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 肝功能（因有肝毒性疑慮）；其餘請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜記錄的禁忌疾病（非仿單內容）**：肝衰竭、肝病、膽囊疾病、高膽紅素血症（含遺傳性及 Gilbert 症候群）、G6PD 缺乏症、高鐵血紅素血症、硫血紅素血症、肝醣儲積症、胱胺酸尿症、半乳糖血症、丙酮酸脫氫酶 E3 缺乏症等。
- **肝毒性**：預測分析指出 flutamide 的肝毒性是任何非腫瘤用途的重要安全疑慮。
- **藥物交互作用**：共記錄 100 筆。重大等級包括 **Dolasetron**、**Cisapride**；中度等級包括 Famotidine、Loperamide、Bisacodyl、Clarithromycin、Levofloxacin、Ondansetron、Palonosetron、Naltrexone、Obeticholic acid、Lactulose 等；輕微等級包括 Metronidazole。

其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的攝護腺纖維瘤及其他多數預測沒有任何臨床試驗或文獻，僅為模型預測，證據等級為 L5。
- 證據較多的「良性生殖系統腫瘤」，文獻並未直接研究該疾病，且同樣屬 L5，加上 flutamide 的肝毒性疑慮，目前不宜推進。

**若要推進需要：**
- 明確定義具體的良性疾病（例如 BPH），再針對該疾病檢索直接證據。
- 補充詳細作用機轉資料。
- 取得香港仿單的警語、禁忌與核准適應症文字。
- 擬定肝功能監測計畫，並評估非腫瘤用途的效益與風險比。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

