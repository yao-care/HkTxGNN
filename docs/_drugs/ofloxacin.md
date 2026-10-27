---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ofloxacin：預測新適應症為高澱粉酶血症 (Hyperamylasemia)（證據等級 L5）。原適應症：傷寒、沙門氏菌症、泌尿道感染、支氣管炎、細菌性肺炎等細菌感染"
monitor_inn: "OFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ofloxacin：從細菌感染症到高澱粉酶血症
{: .text-alpha }

## 一句話總結

Ofloxacin（氧氟沙星）是一種氟喹諾酮類抗菌藥，原本用於傷寒、泌尿道感染、支氣管炎、細菌性肺炎等多種細菌感染。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 傷寒、沙門氏菌症、泌尿道感染、支氣管炎、細菌性肺炎等細菌感染（香港許可證未登載適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ofloxacin 屬於氟喹諾酮類抗菌藥，一般認為是抑制細菌 DNA 旋轉酶 (DNA gyrase) 與拓撲異構酶 IV (topoisomerase IV)，在細菌感染中的療效已被證實。

然而，高澱粉酶血症是一種實驗室檢驗異常，成因多樣（例如胰臟炎、唾液腺疾病、腎功能不全），並非抗菌藥的典型治療標的。從機轉上看，抗菌活性與此病況之間沒有明確關聯。

其他排名前列的預測（多株蛋白高黏滯症候群、先天性無白蛋白血症、血型不合、癌前期血液疾病）也同樣缺乏生物學上的合理連結。因此，高分更可能反映模型在知識圖譜上的關聯，而非實際療效訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（註：在排名第 4 的預測「血型不合」下檢索到 1 篇關於 β 溶血性鏈球菌對 bacitracin 抗藥性鑑定的微生物學論文，與本預測無關，推測為關鍵字誤配，未納入。）

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑，無已取消者。以下列出 5 張主要許可證（許可證資料未登載劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-31349 | TARIVID OPHTHALMIC OINT 0.3%（眼用軟膏） | 未登載 | 未登載 |
| HK-31348 | TARIVID EYE DROPS 0.3%（眼藥水） | 未登載 | 未登載 |
| HK-49145 | OXACIN F.C. TAB 200MG（膜衣錠） | 未登載 | 未登載 |
| HK-50395 | FLOVID 200 TAB 200MG（錠劑） | 未登載 | 未登載 |
| HK-66509 | OFLOXACIN EAR DROPS 0.3% W/V（耳用滴劑） | 未登載 | 未登載 |

其餘許可證涵蓋口服錠劑／膠囊、眼用及耳用製劑。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（來自藥物－疾病關聯資料，非仿單原文），主要包括：
  - 心律相關：長 QT 症候群、尖端扭轉型心律不整
  - 肌肉骨骼：肌腱炎、橫紋肌溶解症、重症肌無力
  - 神經系統：癲癇、周邊神經病變
  - 代謝：糖尿病、糖尿病酮酸中毒、低血鉀
  - 器官功能：肝衰竭、肝病、腎病變／腎功能不全、藥物性肝損傷
  - 血液：血小板減少、白血球減少、貧血
  - 腸道：困難梭狀芽孢桿菌結腸炎
- **藥物交互作用**：資料共 100 筆，以下為部分範例。
  - 重大 (Major)：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone（皮質類固醇，與肌腱風險相關）、Bupropion、Chlorpropamide
  - 中度 (Moderate)：Metformin、Pioglitazone、Acarbose、Canagliflozin（降血糖藥，血糖異常風險）；Famotidine、Loperamide、Acetylsalicylic acid、Calcium acetate 等

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，沒有臨床試驗或文獻佐證（證據等級 L5），且 Ofloxacin 的抗菌機轉與高澱粉酶血症之間沒有合理的生物學連結。
- 高澱粉酶血症屬實驗室指標異常而非獨立疾病，不適合作為抗菌藥的再利用標的。

**若要推進需要：**
- 取得 DrugBank 的完整作用機轉資料，並重新評估機轉連結。
- 取得香港衛生署仿單的警語與禁忌，完成安全性篩選。
- 在高澱粉酶血症及其他排名前列的預測疾病中，補做系統性文獻與臨床試驗檢索。
- 釐清高澱粉酶血症的潛在病因（如胰臟炎），確認是否存在有意義的臨床目標族群。
- 若欲探索再利用，建議優先評估原適應症的鄰近感染性疾病，而非目前的預測清單。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

