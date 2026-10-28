---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 871
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline：預測新適應症為血栓性疾病 (Thrombotic Disease)（證據等級 L5）。原適應症：知識圖譜記錄的關聯為氣喘、支氣管炎、肺氣腫等"
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Theophylline：從氣喘到血栓性疾病
{: .text-alpha }

## 一句話總結

Theophylline（茶鹼）是一種支氣管擴張劑，知識圖譜中記錄的使用方向為氣喘、支氣管炎、肺氣腫等呼吸道疾病。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic Disease)** 有效，但目前**沒有臨床試驗**，所檢索到的文獻也沒有直接研究 theophylline 的抗血栓作用，證據僅停留在模型預測層級（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯為氣喘、支氣管炎、肺氣腫等（本次資料中的香港許可證未載明核准適應症文字） |
| 預測新適應症 | 血栓性疾病 (Thrombotic Disease) |
| TxGNN 預測分數 | 0.9962 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，theophylline 是非選擇性磷酸二酯酶（PDE）抑制劑，也是腺苷受體拮抗劑。

從理論上看，抑制 PDE 會使血小板內 cAMP 上升，可能降低血小板聚集，這是模型給出高分的可能原因。然而腺苷受體拮抗作用可能反過來削弱腺苷本身的抗血小板效果，因此淨效應方向並不確定。

需要特別說明：所檢索到的文獻並未把 theophylline 當作抗血栓藥物來研究。內容多為 ticlopidine 藥動學、血液生物標記的檢測方法、血小板活化測量，以及 theophylline 的偵測感測器。這些文獻無法直接支持此預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為與主題相對較相關的文獻。整體而言，沒有任何一篇直接研究 theophylline 對血栓性疾病的療效。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | 回顧抗血小板藥 ticlopidine 的藥動學，並非 theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | 討論前列腺素、血小板與動脈粥狀硬化；prostacyclin 經 cAMP 抑制血小板聚集 |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 體外研究 | General Pharmacology | milrinone 與腺苷經 cAMP 抑制人類血小板反應，並非 theophylline |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | 觀察性研究 | Rheumatology | 白塞氏病患者血小板與嗜中性球活化與年齡、性別、疾病活動度相關 |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | 觀察性研究 | Inflammatory Bowel Diseases | 發炎性腸道疾病患者血小板－白血球聚集體增加 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 分析／感測器研究 | Analytica Chimica Acta | 開發偵測 theophylline 濃度的電化學適體感測器，與抗血栓療效無關 |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | 方法學研究 | Cells | 抗凝劑與檢體處理對血液 microRNA 定量的影響 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45955 | SLO-THEO CAP 100MG（緩釋） | 未提供 | 未提供 |
| HK-19359 | NUELIN-SR 125 TAB 125MG | 未提供 | 未提供 |
| HK-45832 | NUELIN SR 300 TAB 300MG | 未提供 | 未提供 |
| HK-45831 | NUELIN SR 200 TAB 200MG | 未提供 | 未提供 |
| HK-45954 | SLO-THEO CAP 50MG（緩釋） | 未提供 | 未提供 |

本藥共有 8 張有效的單方許可證，以上列出前 5 張。

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單文字）：高血壓、肝衰竭、癲癇、焦慮症、紫質症、腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、甲狀腺功能低下、消化性潰瘍、開角型青光眼、精神病性疾患、糖尿病及酮酸中毒、良性攝護腺增生、嗜中性球低下與顆粒球缺乏症等。
- **藥物交互作用**（共查得 100 筆，以下列出部分）：
  - 嚴重（Major）：Bupropion
  - 中度（Moderate）：famotidine、ranitidine、cimetidine、omeprazole、rabeprazole、clarithromycin、doxycycline、tetracycline、minocycline、hydrocortisone、dexamethasone、betamethasone、triamcinolone、budesonide、活性碳等
  - 輕微（Minor）：ephedrine

Theophylline 治療濃度範圍狹窄，濃度過高有毒性，且許多交互作用會影響其血中濃度。詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有臨床試驗，也沒有直接研究 theophylline 抗血栓作用的文獻，因此證據等級為 L5。
- 機轉方向不確定（PDE 抑制可能有利，腺苷拮抗可能不利），且 theophylline 治療窗窄、交互作用多，不宜在缺乏支持資料時推進。

**若要推進需要：**
- 補足作用機轉資料，並釐清 PDE 抑制與腺苷拮抗對血小板功能的淨效應
- 進行體外血小板聚集試驗或前臨床抗血栓模型，取得直接證據
- 取得香港衛生署仿單的警語與禁忌資料，進行安全性評估
- 若前臨床結果正向，再設計小型探索性臨床試驗，並納入血中濃度監測與交互作用管理

---

## 附註：其他排名較前的預測方向

| 排名 | 預測疾病 | 預測分數 | 證據等級 | 說明 |
|------|---------|---------|---------|------|
| 2 | 鼻腔疾病 (Nasal Cavity Disease) | 0.9953 | L5 | 有 1 篇小型過敏性鼻炎鼻腔抗原激發研究（PMID 9648963），屬生理反應研究，非臨床療效試驗；無登記試驗 |
| 3 | 喉氣管炎 (Laryngotracheitis) | 0.9951 | L5 | 無文獻、無試驗 |
| 4 | 氣管疾病 (Tracheal Disease) | 0.9949 | L3 | 有氣管平滑肌鬆弛的前臨床研究與犬隻氣管塌陷的回溯性研究，但缺乏人類氣管疾病的直接證據 |
| 5 | 咽炎 (Pharyngitis) | 0.9946 | L5 | 檢索文獻多為大環內酯類抗生素，無可信關聯 |
| 6 | 急性喉咽炎 (Acute Laryngopharyngitis) | 0.9935 | L5 | 無文獻、無試驗 |

註：上表中的證據等級為各預測方向的原始評分，僅供參考。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

