---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 9
---

# Chloramphenicol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Chloramphenicol：從廣譜抗菌治療到結膜炎

## 一句話總結

Chloramphenicol（氯黴素）是廣譜抑菌性抗生素，香港已有 20 張許可證，多為眼藥水與眼用軟膏。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，目前無登記中的臨床試驗，但有 **17 篇文獻**，其中包含多篇隨機對照試驗與 Cochrane 系統性回顧。
結膜炎其實是已知的既有用途，並非真正的新適應症，需先核對本地仿單。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未登載適應症文字 |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L1（依據已發表的隨機對照試驗與 Cochrane 回顧，非已登記的 Phase 3 試驗） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Pack 的 MOA 欄位是空的，以下機轉來自證據分析。Chloramphenicol 是廣譜抑菌性抗生素，抑制細菌 50S 核糖體次單位，涵蓋結膜炎常見的細菌病原。文獻指出，它自 1948 年進入臨床，因已知毒性主要以局部製劑使用。在英國，眼用 chloramphenicol 廣泛用於結膜炎，美國則很少處方。

許多比較性試驗都以它作為結膜炎的對照藥，包括 fusidic acid、framycetin、trimethoprim-polymyxin B、norfloxacin、moxifloxacin 等。1995 年的體外感受性研究也顯示，它對結膜炎與眼瞼炎分離菌的感受性名列前茅。因此這個預測很可能對應的是既有適應症，而不是真正的藥物再利用。

原適應症欄位為空，應視為資料缺漏。在把它當成再利用候選之前，需先確認本地許可證的核准適應症。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT | Acta Ophthalmol | 坦尚尼亞急性結膜炎：fusidic acid 臨床成功率 93%，chloramphenicol 48%，framycetin 74%。作者將差異歸因於 fusidic acid 的體外抗藥率較低 |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | RCT | Acta Ophthalmol | 挪威 38 位家醫的急性結膜炎病人：fusidic acid 每日 2 次與 chloramphenicol 每日 6 次相比，療效無顯著差異 |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT | Acta Ophthalmol | 單盲隨機試驗：fusidic acid 成功率 84%，chloramphenicol 81%。chloramphenicol 組局部刺痛等輕微副作用較多（14% vs 5%） |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT | J Antimicrob Chemother | 230 位疑似細菌性結膜炎病人的隨機雙盲多中心試驗：各組藥物皆有效，副作用很少 |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT | Br J Ophthalmol | 墨西哥砂眼流行區的等效性試驗：比較 2.5% povidone-iodine 與眼用 chloramphenicol 預防新生兒結膜炎 |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | 系統性回顧 | Br J Gen Pract | Cochrane 更新：局部抗生素治療急性細菌性結膜炎，並探討是否適用於基層醫療 |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | 系統性回顧 | Cochrane Database Syst Rev | 預防新生兒眼炎的各種介入措施 |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | 比較研究 | Curr Ther Res | 比較 moxifloxacin 與 chloramphenicol 治療細菌性眼部感染 |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | 安全性回顧 | Drug Saf | 討論局部眼用 chloramphenicol 與再生不良性貧血是否有關，該議題至今仍有爭議 |
| [7671609](https://pubmed.ncbi.nlm.nih.gov/7671609/) | 1995 | 體外感受性研究 | Cornea | 結膜炎與眼瞼炎分離菌對多種局部抗生素的感受性，chloramphenicol 排名最高 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61895 | EUROPHEN EYE DROPS 0.5%W/V | 滴眼液（依品名判斷） | 許可證資料未登載 |
| HK-61645 | VANAFEN OPHTHALMIC OINTMENT 1% W/W | 眼用軟膏（依品名判斷） | 許可證資料未登載 |
| HK-09064 | CHLORAMPHENICOL EYE DROPS 0.5% (FAMAR S.A.) | 滴眼液（依品名判斷） | 許可證資料未登載 |
| HK-64734 | CHLOPHEN EYE DROPS 0.5%W/V | 滴眼液（依品名判斷） | 許可證資料未登載 |
| HK-45559 | CHLOROPH EYE OINT 1% | 眼用軟膏（依品名判斷） | 許可證資料未登載 |

以上為 20 張許可證中的 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中有一項需特別留意的訊號：局部眼用 chloramphenicol 是否與再生不良性貧血有關，仍有爭議（PMID 8800624）。全身性使用的骨髓毒性則是此藥已知的主要風險。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 結膜炎有多篇 RCT 與 Cochrane 回顧支持，且香港已有眼用製劑上市，實質上是既有用途。
- 香港衛生署仿單的警語與禁忌資料尚缺，再生不良性貧血的安全性訊號也需要審視。

**若要推進需要：**
- 取得香港衛生署仿單（PDF），確認核准適應症、警語與禁忌症（此為阻斷性資料缺口）
- 補齊 DrugBank 的作用機轉資料
- 評估局部眼用製劑與再生不良性貧血的風險，並建立監測與病人衛教方式
- 確認 fusidic acid 等試驗中的抗藥性資料是否適用於香港本地流行病學

**其他預測適應症：**
TxGNN 的其餘預測（瀰漫性硬皮症、感染後血管炎、感染後疾患、Chagas 心肌病變等）皆為 **Hold**。這些預測沒有臨床或藥理證據支持。例如硬皮症的文獻只是把 chloramphenicol acetyltransferase (CAT) 報告基因當成實驗工具，並未測試 chloramphenicol 本身。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

