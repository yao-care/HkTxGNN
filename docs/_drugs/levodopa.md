---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 526
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Levodopa：預測新適應症為Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)（證據等級 L5）。原適應症：帕金森氏症及相關帕金森症候群"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Levodopa：從帕金森氏症到 Rasmussen 亞急性腦炎
{: .text-alpha }

## 一句話總結

Levodopa（左旋多巴）是多巴胺前驅物，原本用於帕金森氏症及相關的帕金森症候群。
TxGNN 模型預測它可能對 **Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帕金森氏症及相關帕金森症候群 |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 0.9906 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 19 張／共 19 張） |
| 許可證數 | 19 張（有效 19 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Levodopa 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Levodopa 為多巴胺的代謝前驅物，可穿過血腦屏障，並推測在腦內轉化為多巴胺。這被認為是 levodopa 緩解柏金遜症症狀的機轉。」英文原文："Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease."（[DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb)，版本日期 2026-07-20；查閱日期 2026-11-19）。Levodopa 是一種多巴胺前驅物，用於補充帕金森氏症患者紋狀體中不足的多巴胺。香港市面上的產品包括單方，以及與 carbidopa、benserazide、entacapone 組成的複方。

Rasmussen 腦炎是罕見的單側慢性腦炎，由免疫（T 細胞）介導，特徵為難治性局部癲癇與進行性單側大腦半球萎縮。這與多巴胺缺乏的病理機轉**並無明顯關聯**。

此預測目前僅來自 TxGNN 模型（深度學習）的高分，該分數可能反映模型從相關疾病之間學到的相似性，而非生物學證據。這只是未經驗證的假說。多巴胺補充療法預期無法處理該病的發炎病理或癲癇發作。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 19 張有效許可證（皆為有效，無已註銷）。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-43179 | APO-LEVOCARB TAB 100MG/25MG | 複方 | HIND WING CO LTD | 有效 |
| HK-30945 | MADOPAR HBS CAP "125" CONTROLLED RELEASE | 複方 | ROCHE HONG KONG LIMITED | 有效 |
| HK-15442 | MADOPAR '250' TAB | 複方 | ROCHE HONG KONG LIMITED | 有效 |
| HK-52081 | STALEVO 100/25/200MG TAB | 複方 | LOTUS PHARMACEUTICAL HK LIMITED | 有效 |
| HK-49666 | CARBIDOPA & LEVODOPA TAB 25/100MG (TEVA) | 複方 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 有效 |

上表列出其中 5 張（共 19 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的相對禁忌疾病**（來自藥物－疾病關聯，非仿單原文）：包括閉角型與開角型青光眼、精神疾病（精神病、思覺失調相關疾患）、焦慮症、心肌梗塞與心臟傳導疾病、猝死性心臟驟停、黑色素瘤、癲癇、消化性潰瘍、肝腎疾病、糖尿病與酮酸中毒、姿勢性低血壓、多系統萎縮、藥物引起的異動症等。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用。列出的項目中，中度交互作用包括 epinephrine、ephedrine、bupropion、metronidazole、pyridoxine、metoclopramide、鐵劑，以及多種抗膽鹼藥物（atropine、hyoscyamine、glycopyrronium、dicyclomine 等）。制酸劑（鋁、鈣、鎂鹽類）為輕度交互作用。

仿單的警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅有模型分數支持，沒有臨床試驗、文獻或機轉依據（證據等級 L5）。
- Rasmussen 腦炎是免疫介導的疾病，多巴胺補充療法在病理上缺乏合理的作用路徑。

**若要推進需要：**
- 補充 Levodopa 的作用機轉資料，並釐清與 Rasmussen 腦炎病理的可能連結
- 系統性檢索文獻與臨床試驗，確認是否有任何支持或反對的證據
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 進行前臨床或機轉研究，驗證此假說後再考慮進入臨床評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

