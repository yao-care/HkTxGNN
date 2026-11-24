---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "HEPARIN"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
description: "Heparin：預測新適應症為體染色體隱性蛋白 C 缺乏所致血栓傾向症 (thrombophilia due to protein C deficiency, autosomal recessive)（證據等級 L5）。香港藥劑製品註冊：28 張（有效 27 張）"
---

# Heparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Heparin: 體染色體隱性蛋白 C 缺乏所致血栓傾向症 (thrombophilia due to protein C deficiency, autosomal recessive)
{: .text-alpha }

## 一句話總結

Heparin（肝素）是常用的抗凝血藥物，原本用於肺栓塞、瀰漫性血管內凝血、猛爆性紫斑症等疾病。
TxGNN 模型預測它可能對**體染色體隱性蛋白 C 缺乏所致血栓傾向症 (Thrombophilia due to protein C deficiency, autosomal recessive)** 有效。
目前**沒有臨床試驗與文獻**直接支持這個方向，僅有模型預測與機轉推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 體染色體隱性蛋白 C 缺乏所致血栓傾向症 (thrombophilia due to protein C deficiency, autosomal recessive) |
| TxGNN 預測分數 | 0.9929 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 27 張／共 28 張） |
| 許可證數 | 28 張（有效 27 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Heparin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Heparin 與天然存在的血漿蛋白抗凝血酶 III 交互作用，誘導其發生構形改變，從而顯著增強抗凝血酶 III 的絲胺酸蛋白酶活性，進而抑制參與凝血最終序列的活化凝血因子，特別是 Xa 及 IIa。少量 heparin 可抑制第 Xa 因子，較大量則可抑制凝血酶（第 IIa 因子）。」英文原文："Heparin interacts with the naturally occurring plasma protein, antithrombin III, to induce a conformational change, which markedly enhances the serine protease activity of antithrombin III, thereby inhibiting the activated coagulation factors involved in the closing sequence, particularly Xa and IIa. Small amounts of heparin inhibit Factor Xa, and larger amounts inhibit thrombin (Factor IIa)."（[DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e)，版本日期 2026-05-25；查閱日期 2026-11-19）。就一般藥理而言，Heparin 會增強抗凝血酶 (antithrombin) 對凝血酶與第 Xa 因子的抑制作用，進而降低血液凝固性。

蛋白 C 缺乏症患者因為缺少蛋白 C 的天然抗凝血活性，容易處於高凝血狀態。Heparin 的作用可能部分彌補這項缺失。Heparin 的原適應症包含猛爆性紫斑症，而這正是嚴重（同型合子）蛋白 C 缺乏的重症表現之一，兩者在病理上有關聯。

不過這個推論只建立在模型預測分數與機轉推理上，沒有針對此適應症的試驗或文獻佐證，需要更直接的證據才能確認。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前沒有文獻直接針對此預測適應症。

---

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表，以下列出 5 張主要許可證，其餘許可證未列出。這些許可證的核准適應症文字與劑型欄位皆無資料。

<!-- review:begin hk-lic-20261117-heparin-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 20 張有效的單一成分許可證，」。已更正：HK-55431 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-heparin-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-10765 | HEPARIN (LEO) INJ 1000U/ML | 單一成分 | DKSH HONG KONG LIMITED | 有效 |
| HK-57802 | HEPARIN SODIUM INJ 1,000 IU/ML | 單一成分 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-27750 | MULTIPARIN INJ 5000 UNITS/ML | 單一成分 | LUEN CHEONG HONG LTD | 有效 |
| HK-64529 | VAXCEL HEPARIN SODIUM SOLUTION FOR INJECTION 5000IU/ML | 單一成分 | KOTRA PHARMA (HONG KONG) COMPANY | 有效 |
| HK-15279 | HEPARIN INJ 5000 IU/ML (LEO) | 單一成分 | DKSH HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 28 張）。

<!-- licenses:end -->

另有多張外用乳膏、軟膏許可證（例如 HK-33423、HK-31672、HK-61130），僅供局部使用，不適用於本次全身性適應症的評估。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關聯資料，並非仿單文字）：
  - 出血與凝血相關：血友病、凝血疾病、血小板低下、肝素引起的血小板低下症 (HIT)、抗凝血酶 III 缺乏、顱內出血、腦出血、胎盤早期剝離、Glanzmann 血小板無力症、血小板質的缺陷
  - 消化道：活動性消化性潰瘍、潰瘍性結腸炎、發炎性腸道疾病
  - 其他：肝衰竭、膽道疾病、阻塞性黃疸、骨質疏鬆症、感染性心內膜炎、視網膜疾病（含糖尿病視網膜病變、高血壓視網膜病變）、閉塞性動脈硬化症
- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄，以下為部分範例。
  - 中度：Acetylsalicylic acid（阿斯匹靈）、Glimepiride、Glipizide、Glyburide、Repaglinide、Nateglinide 等降血糖藥物，以及 Fenfluramine、Sibutramine
  - 等級未知：Mesalazine、Doxycycline、Pantoprazole、Calcitriol 等

仿單上的警語與禁忌尚待取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測雖然分數高 (0.9929)，但目前沒有任何臨床試驗或文獻佐證，證據等級僅為 L5。
- 作用機轉資料與香港仿單安全資料尚缺，無法進行安全性篩選。

**若要推進需要：**
- 取得 Heparin 的詳細作用機轉資料（DrugBank）
- 下載並解析香港衛生署的仿單，取得警語與禁忌
- 搜尋 Heparin 用於蛋白 C 缺乏症（含新生兒猛爆性紫斑症）的病例報告、系統性回顧或治療指引
- 與現行標準治療（如蛋白 C 濃縮製劑、維生素 K 拮抗劑）比較其角色
- 評估出血風險及 HIT 風險，並制定監測計畫

---

### 附註：另一個預測適應症（原發性血小板釋放障礙）

模型也預測 Heparin 可能對**原發性血小板釋放障礙 (Primary release disorder of platelets)** 有效（分數 0.9906，證據等級 L5，建議 Hold）。目前沒有臨床試驗，檢索到的文獻多為凝血、HIT、血栓及重症醫學的一般性綜述，並未探討 Heparin 治療此疾病。

血小板釋放障礙屬於出血傾向的血小板功能缺陷，而 Heparin 是增加出血風險的抗凝劑，也可能引起 HIT 等血小板相關併發症。機轉上找不到合理的連結，高分可能來自網絡鄰近性而非真正的治療訊號。在取得直接證據前不建議推進。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「香港共有 20 張有效的單一成分許可證，」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數（含有效、」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

