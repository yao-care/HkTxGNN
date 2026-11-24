---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 857
evidence_level: L5
indication_count: 7
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
last_modified_at: 2026-11-24
description: "Tenecteplase：預測新適應症為Congenital coronary artery anomaly（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Tenecteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## 一句話總結

Tenecteplase 是一種纖維蛋白特異性的血栓溶解劑，知識圖譜中記錄的用途包括心肌梗塞與冠狀動脈血栓。
TxGNN 模型預測它可能對**冠狀動脈狹窄 (Coronary Stenosis)** 有效（預測分數最高者為先天性冠狀動脈異常，但該項無任何證據，故改以證據最多的冠狀動脈狹窄作為主要討論對象）。
目前**無臨床試驗登記**，有 **9 篇文獻**與冠狀動脈相關情境有關，但皆未直接以冠狀動脈狹窄本身為研究對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Congenital coronary artery anomaly |
| TxGNN 預測分數 | 0.9961 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

說明：排名第一的預測為先天性冠狀動脈異常（0.9961），但無任何試驗或文獻，證據等級為 L5。以下以冠狀動脈狹窄為主，並於結論列出其他預測結果。

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Tenecteplase 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Tenecteplase 是人類組織胞漿素原活化劑（tPA）的修飾形式，可與纖維蛋白結合，並將胞漿素原轉化為胞漿素。體外研究顯示，在纖維蛋白存在下，tenecteplase 介導的胞漿素原轉化為胞漿素的程度，相較於無纖維蛋白存在時有所增加。」英文原文："Tenecteplase is a modified form of human tissue plasminogen activator (tPA) that binds to fibrin and converts plasminogen to plasmin. In the presence of fibrin, in vitro studies demonstrate that tenecteplase-mediated conversion of plasminogen to plasmin is increased relative to its conversion in the absence of fibrin."（[DailyMed: Tnkase (tenecteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e647640d-c395-4b4b-a0be-1162f9c21d84)，版本日期 2025-12-15；查閱日期 2026-11-19）。根據已知資訊，Tenecteplase 屬於纖維蛋白特異性的纖維蛋白溶解劑（組織型纖溶酶原活化劑類），能溶解富含纖維蛋白的血栓。

冠狀動脈狹窄常伴隨血栓形成，例如急性心肌梗塞與 PCI 相關血栓。Tenecteplase 的作用目標是血栓成分，而非固定的動脈粥狀硬化狹窄本身。因此，它在狹窄病灶合併急性血栓時可能有用，但這與知識圖譜中已記錄的心肌梗塞用途高度重疊，不能視為獨立的新適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻皆未直接以冠狀動脈狹窄為研究對象，僅涉及相關情境（STEMI、PCI、血栓等）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | 小型隨機可行性/安全性研究 | The American Journal of Cardiology | 40 名 STEMI 患者於初級 PCI 時，隨機接受冠狀動脈內低劑量 Tenecteplase（4 mg）或生理食鹽水，評估可行性與安全性 |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | 比較研究 | Journal of the American College of Cardiology | 比較 Tenecteplase 輔助血管成形術與單用 Tenecteplase 於高風險 STEMI |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | 病例系列/小型介入研究 | Journal of the American College of Cardiology | 冠狀動脈內纖維蛋白特異性溶栓輸注，協助慢性完全阻塞病灶的經皮再通 |
| [17102829](https://pubmed.ncbi.nlm.nih.gov/17102829/) | 2006 | 觀察性先導研究 | Canadian Journal of Cardiology | 溶栓後轉院進行緊急 PCI 的可行性 |
| [11994554](https://pubmed.ncbi.nlm.nih.gov/11994554/) | 2002 | 觀察性研究 | Journal of Thrombosis and Thrombolysis | 下壁心肌梗塞中胸前導程 ST 段下降與非罪犯血管血流緩慢相關 |
| [23615379](https://pubmed.ncbi.nlm.nih.gov/23615379/) | 2013 | 回顧 | Cerebrovascular Diseases | 急性缺血性中風溶栓治療的歷史與未來（間接相關） |
| [37823944](https://pubmed.ncbi.nlm.nih.gov/37823944/) | 2023 | 病例報告 | Egyptian Heart Journal | 氯吡格雷抵抗導致亞急性支架血栓 |
| [25733729](https://pubmed.ncbi.nlm.nih.gov/25733729/) | 2016 | 病例報告 | Human & Experimental Toxicology | 一氧化碳中毒後的下側壁心肌梗塞接受溶栓治療 |
| [31020237](https://pubmed.ncbi.nlm.nih.gov/31020237/) | 2019 | 病例報告 | European Heart Journal – Case Reports | 以支架回收器取出擴張冠狀動脈中的難治性血栓 |

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-49440 | METALYSE FOR INJ 10,000U | 單一成分 | BOEHRINGER INGELHEIM (HK) LTD | 有效 |

上表列出其中 1 張（共 2 張）。

<!-- licenses:end -->

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分重點。
  - 重大（Major）：Abciximab、Apixaban、Betrixaban、Acalabrutinib、Avapritinib、Deferasirox、Ibritumomab tiuxetan、Tositumomab
  - 中度（Moderate）：Acetylsalicylic acid、Ibuprofen、Ketorolac、Celecoxib、Aminocaproic acid、Omega-3 fatty acids、Fenfluramine、Dexfenfluramine、Sibutramine

  多數重大交互作用涉及出血風險增加（抗凝血或抗血小板類藥物），使用時需特別留意。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何已發表研究直接針對「冠狀動脈狹窄」本身，現有文獻多為 STEMI/PCI 情境的早期研究與病例報告，因此證據等級為 L5。
- 與狹窄相關的用途大多與知識圖譜已記錄的心肌梗塞用途重疊，作為獨立新適應症的證據薄弱，且出血風險需先評估。

**若要推進需要：**
- 取得 Tenecteplase 的作用機轉資料
- 取得香港仿單的核准適應症、警語與禁忌症
- 設計直接針對冠狀動脈狹窄（並區分血栓成分）的臨床研究
- 建立出血風險評估與監測計畫，特別是併用抗凝血或抗血小板藥物時

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Tnkase (tenecteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e647640d-c395-4b4b-a0be-1162f9c21d84) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

