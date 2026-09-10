---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Linaclotide：從腸躁症/慢性便秘到馬尾症候群

## 一句話總結

Linaclotide 是腸道局部作用的 guanylate cyclase-C (GC-C) 促效劑，全身吸收極低，原本用於刺激腸液分泌、加速腸蠕動，屬 IBS-C（腸躁症合併便秘）/CIC（慢性特發性便秘）用藥。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻支持**，機轉上也找不到合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸躁症合併便秘 (IBS-C) / 慢性特發性便秘 (CIC)（依作用機轉推論，原始適應症欄位無資料） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（[Data Gap]）。根據 evidence pack 中的機轉推論，Linaclotide 是 GC-C 促效劑，作用侷限於腸上皮，全身吸收極低，用於刺激腸液分泌與腸蠕動。

馬尾症候群是神經外科急症，成因為神經根壓迫導致的腸道、膀胱與下肢功能障礙，與 GC-C 訊號路徑沒有已知的病理生理連結。TxGNN 給出的高分（99.96%）較可能反映知識圖譜中「便秘為馬尾症候群常見伴隨症狀」所造成的共病關聯偏誤，而非真實的藥理因果機轉。

模型同時預測的另外兩個適應症——神經性膀胱（節點已標註為 obsolete，屬低品質圖譜節點）與失眠（Linaclotide 幾乎不通過血腦障壁，缺乏中樞作用基礎）——同樣缺乏機轉支持，顯示這組預測整體可信度偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 結論與下一步

**決策：Hold**

**理由：**
三個預測適應症（馬尾症候群、神經性膀胱、失眠）皆為 L5（僅有模型預測，無任何臨床試驗或文獻），且機轉分析明確指出無直接因果連結，判斷為知識圖譜共病關聯所致的偏誤預測，不建議推進。

**若要推進需要：**
- 補齊 Linaclotide 的正式作用機轉（MOA）與原始核准適應症資料
- 取得 TFDA/香港仿單警語與禁忌症，解除 S1 安全性初評的阻斷（DG001）
- 若未來出現支持性臨床或機轉文獻，重新評估證據等級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

